from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Education(models.Model):
    """Model describing education experience"""

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Студент",
        db_index=True,
    )
    university = models.CharField(
        "ВУЗ",
        max_length=settings.USER_MODEL_MAX_LEN,
        help_text="Название учебного заведения",
    )
    start_date = models.DateField(
        "Дата поступления",
        help_text="Дата поступления",
    )
    end_date = models.DateField(
        "Дата окончания",
        default=timezone.now(),
        null=True,
        blank=True,  # Если пусто - по настоящее время
        help_text="Дата окончания",
    )
    faculty = models.CharField(
        "Факультет",
        blank=True,
        max_length=settings.USER_MODEL_MAX_LEN,
        help_text="Ваш факультет",
    )
    speciality = models.CharField(
        "Специальность",
        max_length=settings.USER_MODEL_MAX_LEN,
        help_text="Ваша специальность",
    )
    grade = models.CharField(
        "Степень",
        blank=True,
        choices=settings.GRADE,
        max_length=settings.USER_MODEL_MAX_LEN,
        help_text="Ваша степень",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "university", "start_date", "end_date"],
                name="unique_university_in_one_time",
            ),
            models.CheckConstraint(
                check=models.Q(end_date__gt=models.F("start_date")),
                name="check_education_end_date",
                violation_error_message=(
                    "Дата окончания обучения должна " "быть позже начала!"
                ),
            ),
        ]
        default_related_name = "educations"
        verbose_name = "Образование"
        verbose_name_plural = "Образование"
        ordering = ("university",)

    def __str__(self):
        return (
            f"{self.student.get_full_name()} получал "
            f'образование по специальности "{self.speciality}"'
            f' в "{self.university}"'
        )
