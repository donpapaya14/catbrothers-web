"""
Planifica temas evitando duplicados y rotando categorías.
Lee artículos existentes en src/content/blog/ para evitar repetir.
"""

import os
import random
import re
from pathlib import Path

BLOG_DIR = Path(__file__).parent.parent / "src" / "content" / "blog"

CATEGORIES = ["salud-felina", "alimentacion", "juguetes", "comportamiento", "productos"]

ARTICLE_FORMULAS = {
    "salud-felina": [
        "Enfermedad común en gatos con síntomas, causas y tratamiento según veterinarios con estudio real",
        "Vacunas esenciales para gatos: cuáles, cuándo y por qué según protocolos veterinarios actualizados",
        "Señales de que tu gato está enfermo que la mayoría ignora, con datos de estudios veterinarios",
        "Cuidados dentales para gatos: guía completa con recomendaciones de la AVMA",
    ],
    "alimentacion": [
        "Comparativa de marcas de comida para gatos con análisis nutricional REAL (proteínas, cenizas, ingredientes)",
        "Alimentos tóxicos para gatos: lista completa con nivel de toxicidad según ASPCA",
        "Dieta húmeda vs seca para gatos: qué dice la ciencia veterinaria con estudios reales",
        "Mejor alimentación para gatos esterilizados según necesidades calóricas reales",
    ],
    "juguetes": [
        "Los mejores juguetes interactivos para gatos: nombres reales, precios, dónde comprar y por qué funcionan",
        "Juguetes caseros para gatos: 5 ideas con materiales de casa y explicación de por qué estimulan",
        "Rascadores para gatos: tipos, materiales y cuál elegir según tamaño y comportamiento del gato",
    ],
    "comportamiento": [
        "Por qué tu gato hace X (comportamiento específico): explicación científica del comportamiento felino",
        "Cómo socializar gatos que no se llevan bien: técnicas de Jackson Galaxy con pasos concretos",
        "Lenguaje corporal de los gatos: guía visual de lo que significan cola, orejas, pupilas y posturas",
        "Estrés en gatos: causas, señales y soluciones respaldadas por etología felina",
    ],
    "productos": [
        "Review de producto específico para gatos de Amazon con pros, contras y comparativa con alternativas",
        "Los 5 mejores areneros para gatos: comparativa real con precios y experiencia de uso",
        "Mejores transportines para gatos: comparativa con medidas, materiales y enlaces de compra",
    ],
}
