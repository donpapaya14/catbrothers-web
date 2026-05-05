export const CATEGORIES = {
  'cat-health': { name: 'Cat Health', slug: 'cat-health', description: 'Keep your cat healthy with vet-backed tips' },
  'nutrition': { name: 'Cat Nutrition', slug: 'nutrition', description: 'Best food for cats based on real science' },
  'behavior': { name: 'Cat Behavior', slug: 'behavior', description: 'Understand your cat like never before' },
  'products': { name: 'Cat Products', slug: 'products', description: 'Top cat products reviewed' },
  'entertainment': { name: 'Cat Fun Facts', slug: 'entertainment', description: 'Fascinating cat facts' }
} as const;

export type Category = keyof typeof CATEGORIES;

export function getCategoryName(cat: Category): string {
  return CATEGORIES[cat].name;
}

export function getCategoryBadgeClass(cat: Category): string {
  return `badge badge--${cat}`;
}
