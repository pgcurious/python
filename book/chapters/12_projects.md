# Chapter 12: Practical Projects

This final chapter brings everything together with complete, practical projects. Each project reinforces concepts from previous chapters.

## Project 1: Command-Line Task Manager

A task manager CLI application demonstrating file I/O, classes, and user interaction.

### Features
- Add, list, complete, and delete tasks
- Persistent storage (JSON)
- Priority levels and due dates
- Search and filter

```python
#!/usr/bin/env python3
"""
Task Manager CLI - A command-line task management application.
"""

import json
import argparse
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    priority: Priority = Priority.MEDIUM
    due_date: Optional[str] = None
    completed: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self):
        d = asdict(self)
        d["priority"] = self.priority.name
        return d

    @classmethod
    def from_dict(cls, data):
        data["priority"] = Priority[data["priority"]]
        return cls(**data)


class TaskManager:
    def __init__(self, storage_path: str = "tasks.json"):
        self.storage_path = Path(storage_path)
        self.tasks: list[Task] = []
        self._load()

    def _load(self):
        if self.storage_path.exists():
            data = json.loads(self.storage_path.read_text())
            self.tasks = [Task.from_dict(t) for t in data]

    def _save(self):
        data = [t.to_dict() for t in self.tasks]
        self.storage_path.write_text(json.dumps(data, indent=2))

    def _next_id(self) -> int:
        return max((t.id for t in self.tasks), default=0) + 1

    def add(self, title: str, description: str = "",
            priority: Priority = Priority.MEDIUM,
            due_date: Optional[str] = None) -> Task:
        task = Task(
            id=self._next_id(),
            title=title,
            description=description,
            priority=priority,
            due_date=due_date
        )
        self.tasks.append(task)
        self._save()
        return task

    def list(self, show_completed: bool = False,
             priority: Optional[Priority] = None) -> list[Task]:
        tasks = self.tasks
        if not show_completed:
            tasks = [t for t in tasks if not t.completed]
        if priority:
            tasks = [t for t in tasks if t.priority == priority]
        return sorted(tasks, key=lambda t: (-t.priority.value, t.created_at))

    def complete(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self._save()
                return task
        return None

    def delete(self, task_id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self._save()
                return True
        return False

    def search(self, query: str) -> list[Task]:
        query = query.lower()
        return [t for t in self.tasks
                if query in t.title.lower() or query in t.description.lower()]


def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("-d", "--description", default="")
    add_parser.add_argument("-p", "--priority",
                           choices=["low", "medium", "high"],
                           default="medium")
    add_parser.add_argument("--due", help="Due date (YYYY-MM-DD)")

    # List command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("-a", "--all", action="store_true",
                            help="Show completed tasks")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark task complete")
    complete_parser.add_argument("id", type=int, help="Task ID")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search tasks")
    search_parser.add_argument("query", help="Search query")

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add":
        priority = Priority[args.priority.upper()]
        task = manager.add(args.title, args.description, priority, args.due)
        print(f"Added task #{task.id}: {task.title}")

    elif args.command == "list":
        tasks = manager.list(show_completed=args.all)
        if not tasks:
            print("No tasks found.")
        for task in tasks:
            status = "✓" if task.completed else " "
            print(f"[{status}] #{task.id} [{task.priority.name}] {task.title}")

    elif args.command == "complete":
        task = manager.complete(args.id)
        if task:
            print(f"Completed: {task.title}")
        else:
            print(f"Task #{args.id} not found")

    elif args.command == "delete":
        if manager.delete(args.id):
            print(f"Deleted task #{args.id}")
        else:
            print(f"Task #{args.id} not found")

    elif args.command == "search":
        tasks = manager.search(args.query)
        for task in tasks:
            print(f"#{task.id} {task.title}")


if __name__ == "__main__":
    main()
```

---

## Project 2: Web Scraper with Data Export

A web scraper that extracts data and exports to multiple formats.

```python
#!/usr/bin/env python3
"""
Web Scraper - Extract structured data from websites.
Requires: pip install requests beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
from dataclasses import dataclass, asdict
from typing import Generator
from pathlib import Path
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Article:
    title: str
    url: str
    summary: str
    date: str = ""
    author: str = ""


class WebScraper:
    def __init__(self, base_url: str, delay: float = 1.0):
        self.base_url = base_url
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Educational Scraper)"
        })

    def fetch_page(self, url: str) -> BeautifulSoup:
        """Fetch and parse a webpage."""
        logger.info(f"Fetching: {url}")
        time.sleep(self.delay)

        response = self.session.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def extract_articles(self, soup: BeautifulSoup) -> Generator[Article, None, None]:
        """Extract articles from page - customize for target site."""
        # Example: Extract from a blog-like structure
        for article in soup.find_all("article"):
            title_elem = article.find("h2")
            link_elem = article.find("a")
            summary_elem = article.find("p", class_="summary")
            date_elem = article.find("time")

            if title_elem and link_elem:
                yield Article(
                    title=title_elem.get_text(strip=True),
                    url=link_elem.get("href", ""),
                    summary=summary_elem.get_text(strip=True) if summary_elem else "",
                    date=date_elem.get("datetime", "") if date_elem else ""
                )

    def scrape(self, pages: int = 1) -> list[Article]:
        """Scrape multiple pages."""
        articles = []
        for page in range(1, pages + 1):
            url = f"{self.base_url}?page={page}"
            try:
                soup = self.fetch_page(url)
                articles.extend(self.extract_articles(soup))
            except Exception as e:
                logger.error(f"Error scraping {url}: {e}")
        return articles


class DataExporter:
    """Export data to various formats."""

    @staticmethod
    def to_json(articles: list[Article], filepath: str):
        data = [asdict(a) for a in articles]
        Path(filepath).write_text(json.dumps(data, indent=2))
        logger.info(f"Exported {len(articles)} articles to {filepath}")

    @staticmethod
    def to_csv(articles: list[Article], filepath: str):
        if not articles:
            return

        fieldnames = list(asdict(articles[0]).keys())
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(asdict(a) for a in articles)
        logger.info(f"Exported {len(articles)} articles to {filepath}")

    @staticmethod
    def to_markdown(articles: list[Article], filepath: str):
        lines = ["# Scraped Articles\n"]
        for article in articles:
            lines.append(f"## [{article.title}]({article.url})\n")
            if article.date:
                lines.append(f"*{article.date}*\n")
            lines.append(f"{article.summary}\n")
            lines.append("---\n")

        Path(filepath).write_text("\n".join(lines))
        logger.info(f"Exported {len(articles)} articles to {filepath}")


def main():
    # Example usage
    scraper = WebScraper("https://example-blog.com/articles")
    articles = scraper.scrape(pages=3)

    exporter = DataExporter()
    exporter.to_json(articles, "articles.json")
    exporter.to_csv(articles, "articles.csv")
    exporter.to_markdown(articles, "articles.md")


if __name__ == "__main__":
    main()
```

---

## Project 3: REST API with Flask

A simple REST API demonstrating web development basics.

```python
#!/usr/bin/env python3
"""
Simple REST API with Flask.
Requires: pip install flask
"""

from flask import Flask, request, jsonify
from dataclasses import dataclass, asdict
from typing import Optional
import uuid

app = Flask(__name__)


@dataclass
class Book:
    id: str
    title: str
    author: str
    year: int
    isbn: Optional[str] = None


# In-memory storage
books: dict[str, Book] = {}


# Sample data
def init_sample_data():
    sample_books = [
        Book(str(uuid.uuid4()), "The Python Book", "Jane Smith", 2023),
        Book(str(uuid.uuid4()), "Learning Flask", "John Doe", 2022),
    ]
    for book in sample_books:
        books[book.id] = book


@app.route("/api/books", methods=["GET"])
def get_books():
    """Get all books with optional filtering."""
    author = request.args.get("author")
    year = request.args.get("year", type=int)

    result = list(books.values())

    if author:
        result = [b for b in result if author.lower() in b.author.lower()]
    if year:
        result = [b for b in result if b.year == year]

    return jsonify([asdict(b) for b in result])


@app.route("/api/books/<book_id>", methods=["GET"])
def get_book(book_id):
    """Get a single book by ID."""
    book = books.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(asdict(book))


@app.route("/api/books", methods=["POST"])
def create_book():
    """Create a new book."""
    data = request.get_json()

    if not data or "title" not in data or "author" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    book = Book(
        id=str(uuid.uuid4()),
        title=data["title"],
        author=data["author"],
        year=data.get("year", 2024),
        isbn=data.get("isbn")
    )
    books[book.id] = book
    return jsonify(asdict(book)), 201


@app.route("/api/books/<book_id>", methods=["PUT"])
def update_book(book_id):
    """Update an existing book."""
    if book_id not in books:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json()
    book = books[book_id]

    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.year = data.get("year", book.year)
    book.isbn = data.get("isbn", book.isbn)

    return jsonify(asdict(book))


@app.route("/api/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    """Delete a book."""
    if book_id not in books:
        return jsonify({"error": "Book not found"}), 404

    del books[book_id]
    return "", 204


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    init_sample_data()
    app.run(debug=True, port=5000)
```

---

## Project 4: Data Analysis Script

A data analysis script using only standard library tools.

```python
#!/usr/bin/env python3
"""
Sales Data Analyzer - Analyze CSV sales data.
"""

import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from statistics import mean, median, stdev
from typing import Generator


@dataclass
class Sale:
    date: datetime
    product: str
    category: str
    quantity: int
    price: float
    region: str

    @property
    def total(self) -> float:
        return self.quantity * self.price


class SalesAnalyzer:
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.sales: list[Sale] = []
        self._load_data()

    def _load_data(self):
        with open(self.filepath, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.sales.append(Sale(
                    date=datetime.strptime(row["date"], "%Y-%m-%d"),
                    product=row["product"],
                    category=row["category"],
                    quantity=int(row["quantity"]),
                    price=float(row["price"]),
                    region=row["region"]
                ))

    def total_revenue(self) -> float:
        return sum(sale.total for sale in self.sales)

    def revenue_by_category(self) -> dict[str, float]:
        by_category = defaultdict(float)
        for sale in self.sales:
            by_category[sale.category] += sale.total
        return dict(sorted(by_category.items(), key=lambda x: -x[1]))

    def revenue_by_region(self) -> dict[str, float]:
        by_region = defaultdict(float)
        for sale in self.sales:
            by_region[sale.region] += sale.total
        return dict(by_region)

    def top_products(self, n: int = 10) -> list[tuple[str, float]]:
        by_product = defaultdict(float)
        for sale in self.sales:
            by_product[sale.product] += sale.total
        sorted_products = sorted(by_product.items(), key=lambda x: -x[1])
        return sorted_products[:n]

    def monthly_trend(self) -> dict[str, float]:
        by_month = defaultdict(float)
        for sale in self.sales:
            month_key = sale.date.strftime("%Y-%m")
            by_month[month_key] += sale.total
        return dict(sorted(by_month.items()))

    def statistics(self) -> dict:
        totals = [sale.total for sale in self.sales]
        return {
            "count": len(self.sales),
            "total_revenue": sum(totals),
            "average_sale": mean(totals),
            "median_sale": median(totals),
            "std_dev": stdev(totals) if len(totals) > 1 else 0,
            "max_sale": max(totals),
            "min_sale": min(totals)
        }

    def generate_report(self) -> str:
        lines = ["# Sales Analysis Report", ""]

        stats = self.statistics()
        lines.append("## Summary Statistics")
        lines.append(f"- Total Sales: {stats['count']:,}")
        lines.append(f"- Total Revenue: ${stats['total_revenue']:,.2f}")
        lines.append(f"- Average Sale: ${stats['average_sale']:.2f}")
        lines.append(f"- Median Sale: ${stats['median_sale']:.2f}")
        lines.append("")

        lines.append("## Revenue by Category")
        for category, revenue in self.revenue_by_category().items():
            lines.append(f"- {category}: ${revenue:,.2f}")
        lines.append("")

        lines.append("## Top 5 Products")
        for product, revenue in self.top_products(5):
            lines.append(f"- {product}: ${revenue:,.2f}")
        lines.append("")

        lines.append("## Monthly Trend")
        for month, revenue in self.monthly_trend().items():
            lines.append(f"- {month}: ${revenue:,.2f}")

        return "\n".join(lines)


def create_sample_data(filepath: str):
    """Create sample CSV data for testing."""
    import random

    products = [
        ("Laptop", "Electronics", 999.99),
        ("Phone", "Electronics", 699.99),
        ("Headphones", "Electronics", 149.99),
        ("Desk", "Furniture", 299.99),
        ("Chair", "Furniture", 199.99),
        ("Book", "Books", 19.99),
        ("Notebook", "Office", 9.99),
    ]
    regions = ["North", "South", "East", "West"]

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "product", "category", "quantity", "price", "region"])

        for month in range(1, 13):
            for _ in range(random.randint(50, 100)):
                product, category, price = random.choice(products)
                day = random.randint(1, 28)
                writer.writerow([
                    f"2024-{month:02d}-{day:02d}",
                    product,
                    category,
                    random.randint(1, 5),
                    price,
                    random.choice(regions)
                ])


def main():
    data_file = "sales_data.csv"

    # Create sample data if doesn't exist
    if not Path(data_file).exists():
        print("Creating sample data...")
        create_sample_data(data_file)

    analyzer = SalesAnalyzer(data_file)
    report = analyzer.generate_report()
    print(report)

    # Save report
    Path("sales_report.md").write_text(report)
    print("\nReport saved to sales_report.md")


if __name__ == "__main__":
    main()
```

---

## Project 5: File Organizer

Automatically organize files by type, date, or custom rules.

```python
#!/usr/bin/env python3
"""
File Organizer - Organize files by type, date, or custom rules.
"""

import shutil
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass
from typing import Callable
import logging
import argparse

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


# File type categories
FILE_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx"},
    "Videos": {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".go"},
    "Data": {".json", ".csv", ".xml", ".yaml", ".yml", ".sql"},
}


@dataclass
class OrganizeRule:
    name: str
    matcher: Callable[[Path], bool]
    destination: Callable[[Path], Path]


class FileOrganizer:
    def __init__(self, source_dir: str, target_dir: str = None):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir) if target_dir else self.source_dir
        self.rules: list[OrganizeRule] = []
        self.dry_run = False

    def add_category_rules(self):
        """Add rules based on file categories."""
        for category, extensions in FILE_CATEGORIES.items():
            self.rules.append(OrganizeRule(
                name=f"Category: {category}",
                matcher=lambda p, ext=extensions: p.suffix.lower() in ext,
                destination=lambda p, cat=category: self.target_dir / cat / p.name
            ))

    def add_date_rules(self):
        """Organize files by modification date."""
        def get_date_path(path: Path) -> Path:
            mtime = datetime.fromtimestamp(path.stat().st_mtime)
            return self.target_dir / mtime.strftime("%Y/%m") / path.name

        self.rules.append(OrganizeRule(
            name="By Date",
            matcher=lambda p: True,
            destination=get_date_path
        ))

    def add_size_rules(self):
        """Organize files by size."""
        def get_size_category(path: Path) -> str:
            size = path.stat().st_size
            if size < 1024 * 1024:  # < 1MB
                return "Small"
            elif size < 100 * 1024 * 1024:  # < 100MB
                return "Medium"
            else:
                return "Large"

        self.rules.append(OrganizeRule(
            name="By Size",
            matcher=lambda p: True,
            destination=lambda p: self.target_dir / get_size_category(p) / p.name
        ))

    def get_files(self) -> list[Path]:
        """Get all files in source directory."""
        return [f for f in self.source_dir.iterdir() if f.is_file()]

    def find_destination(self, file_path: Path) -> Path | None:
        """Find destination for a file based on rules."""
        for rule in self.rules:
            if rule.matcher(file_path):
                return rule.destination(file_path)
        return None

    def organize(self, dry_run: bool = False) -> dict:
        """Organize files according to rules."""
        self.dry_run = dry_run
        results = {"moved": [], "skipped": [], "errors": []}

        for file_path in self.get_files():
            dest = self.find_destination(file_path)

            if not dest:
                results["skipped"].append(file_path)
                continue

            if dest == file_path:
                results["skipped"].append(file_path)
                continue

            try:
                if not dry_run:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(file_path), str(dest))

                results["moved"].append((file_path, dest))
                logger.info(f"{'Would move' if dry_run else 'Moved'}: {file_path.name} -> {dest}")

            except Exception as e:
                results["errors"].append((file_path, str(e)))
                logger.error(f"Error moving {file_path}: {e}")

        return results

    def preview(self):
        """Preview organization without making changes."""
        return self.organize(dry_run=True)


def main():
    parser = argparse.ArgumentParser(description="Organize files automatically")
    parser.add_argument("source", help="Source directory")
    parser.add_argument("-t", "--target", help="Target directory (default: source)")
    parser.add_argument("-m", "--mode", choices=["category", "date", "size"],
                       default="category", help="Organization mode")
    parser.add_argument("-n", "--dry-run", action="store_true",
                       help="Preview without moving files")

    args = parser.parse_args()

    organizer = FileOrganizer(args.source, args.target)

    if args.mode == "category":
        organizer.add_category_rules()
    elif args.mode == "date":
        organizer.add_date_rules()
    elif args.mode == "size":
        organizer.add_size_rules()

    results = organizer.organize(dry_run=args.dry_run)

    print(f"\n{'Preview' if args.dry_run else 'Summary'}:")
    print(f"  Moved: {len(results['moved'])}")
    print(f"  Skipped: {len(results['skipped'])}")
    print(f"  Errors: {len(results['errors'])}")


if __name__ == "__main__":
    main()
```

---

## What's Next?

Congratulations on completing this Python book! Here are some directions to continue learning:

### Explore Specialized Domains
- **Web Development**: Django, FastAPI, Flask
- **Data Science**: Pandas, NumPy, Matplotlib, Scikit-learn
- **Machine Learning**: TensorFlow, PyTorch
- **Automation**: Selenium, Playwright
- **DevOps**: Docker, Kubernetes with Python

### Deepen Your Python Knowledge
- **Advanced Topics**: Metaclasses, descriptors, async/await
- **Performance**: Profiling, Cython, PyPy
- **Code Quality**: Type checking with mypy, linting with ruff

### Build More Projects
- Personal portfolio website
- Discord/Slack bot
- Automation scripts for your workflow
- Contribution to open source

### Resources
- Python Official Documentation: docs.python.org
- Real Python: realpython.com
- Python Weekly Newsletter
- PyCon Talks on YouTube

Happy coding! 🐍
