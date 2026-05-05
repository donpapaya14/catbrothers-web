"""
Plans topics avoiding duplicates and rotating categories.
Reads existing articles in src/content/blog/ to avoid repetition.
"""

import random
import re
from pathlib import Path

BLOG_DIR = Path(__file__).parent.parent / "src" / "content" / "blog"

CATEGORIES = ["cat-health", "nutrition", "behavior", "products", "entertainment"]

ARTICLE_FORMULAS = {
    "cat-health": [
        "Common cat disease with symptoms, causes and treatment according to veterinary studies",
        "Essential vaccines for cats: which ones, when and why according to AVMA protocols",
        "Cat health warning signs most owners miss, with data from veterinary studies",
        "Dental care for cats: complete guide with AVMA recommendations",
        "Cat age and lifespan: what affects how long cats live with real research data",
        "Signs your cat is in pain: subtle signals and what vets recommend",
    ],
    "nutrition": [
        "Cat food brand comparison with REAL nutritional analysis (protein, ash, ingredients)",
        "Foods toxic to cats: complete list with toxicity level according to ASPCA",
        "Wet vs dry food for cats: what veterinary science says with real studies",
        "Best diet for sterilized cats according to real caloric needs",
        "Reading cat food labels: what every ingredient means and what to avoid",
        "Raw diet for cats: evidence, risks and vet consensus explained",
    ],
    "behavior": [
        "Why cats do X (specific behavior): scientific explanation of feline behavior",
        "How to socialize cats that don't get along: techniques with concrete steps",
        "Cat body language guide: what tail, ears, pupils and postures actually mean",
        "Stress in cats: causes, signs and solutions backed by feline ethology",
        "Why cats knock things off tables: real science behind this behavior",
        "Cat kneading behavior explained: evolutionary and emotional reasons",
    ],
    "products": [
        "Review of specific Amazon cat product with pros, cons and comparison to alternatives",
        "Best litter boxes for cats: real comparison with prices and real usage experience",
        "Best cat carriers: comparison with dimensions, materials and purchase links",
        "Interactive cat toys that actually work: science of feline play explained",
        "Cat water fountains: why cats prefer running water and best options reviewed",
    ],
    "entertainment": [
        "Famous cat from history with verified story and real facts (Félicette, Unsinkable Sam, etc.)",
        "Surprising cat fact backed by science that most people don't know",
        "Cat world record or extreme fact with verified source",
        "Cat vs human senses comparison: specific numbers for vision, hearing and smell",
        "Domestic cats vs wild cats: specific behavioral difference with evolutionary reason",
    ],
}


def get_existing_titles() -> set[str]:
    titles = set()
    if not BLOG_DIR.exists():
        return titles
    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        if match:
            titles.add(match.group(1).lower().strip())
    return titles


def get_category_counts() -> dict[str, int]:
    counts = {cat: 0 for cat in CATEGORIES}
    if not BLOG_DIR.exists():
        return counts
    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^category:\s*["\']?([^"\'\n]+)["\']?\s*$', content, re.MULTILINE)
        if match and match.group(1).strip() in counts:
            counts[match.group(1).strip()] += 1
    return counts


def pick_category() -> str:
    counts = get_category_counts()
    min_count = min(counts.values())
    least_covered = [cat for cat, count in counts.items() if count == min_count]
    return random.choice(least_covered)


def pick_formula(category: str) -> str:
    formulas = ARTICLE_FORMULAS.get(category, list(ARTICLE_FORMULAS.values())[0])
    return random.choice(formulas)


def plan_topic() -> dict:
    category = pick_category()
    formula = pick_formula(category)
    existing = get_existing_titles()
    return {
        "category": category,
        "formula": formula,
        "existing_titles": list(existing)[:20],
        "existing_count": len(existing),
    }
