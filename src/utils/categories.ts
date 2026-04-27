export const CATEGORIES = {
  'salud-felina': { name: 'Salud Felina', slug: 'salud-felina', description: 'Cuidados y salud de tu gato' },
  'alimentacion': { name: 'Alimentacion', slug: 'alimentacion', description: 'Mejor comida para gatos con datos reales' },
  'juguetes': { name: 'Juguetes', slug: 'juguetes', description: 'Los mejores juguetes para gatos' },
  'comportamiento': { name: 'Comportamiento', slug: 'comportamiento', description: 'Entiende a tu gato como nunca' },
  'productos': { name: 'Productos', slug: 'productos', description: 'Reviews de productos para gatos' },
} as const;

export type Category = keyof typeof CATEGORIES;

export function getCategoryName(cat: Category): string {
  return CATEGORIES[cat].name;
}

export function getCategoryBadgeClass(cat: Category): string {
  return `badge badge--${cat}`;
}
