from django.db import models

class CategoryChoices(models.TextChoices):
    PAINTING = "PAINTING", "Painting"
    TILING = "TILING", "Tiling"
    PLUMBING = "PLUMBING", "Plumbing"
    ELECTRICAL = "ELECTRICAL", "Electrical"
    CARPENTRY = "CARPENTRY", "Carpentry"
    FLOORING = "FLOORING", "Flooring"
    DRYWALL = "DRYWALL", "Drywall Installation & Repair"
    RENOVATION = "RENOVATION", "Home Renovation"
    MASONRY = "MASONRY", "Masonry & Brickwork"
    GENERAL_REPAIR = "GENERAL_REPAIR", "General Repair & Maintenance"
