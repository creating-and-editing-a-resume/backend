from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class EmploymentHistory(models.Model):
    """Model describing work experience"""

    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Работник",
        db_index=True,
    )
    company = models.CharField(
        "Организация",
        max_length=settings.USER_MODEL_MAX_LEN,
        help_text="Название организации",
    )
    web_page = models.URLField(
        "Сайт",
        blank=True,
        help_text="Ссылка на сайт организации",
    )
    position = models.CharField(
        "Должность",
        max_length=settings.USER_MODEL_MAX_LEN,
        help_text="Ваша должность в компании",
    )
    start_date = models.DateField(
        "Дата начала работы",
        help_text="Дата начала работы",
    )
    end_date = models.DateField(
        "Дата окончания работы",
        default=timezone.now(),
        null=True,
        blank=True,  # Если пусто - по настоящее время
        help_text="Дата окончания работы",
    )
    responsibilities = models.TextField(
        "Ваши обязанности и достижения",
        help_text="Перечислите ваши обязанности и достижения",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "company", "position"],
                name="unique_work_in_one_company",
            ),
            models.CheckConstraint(
                check=models.Q(end_date__gt=models.F("start_date")),
                name="check_work_end_date",
                violation_error_message=(
                    "Дата окончания работы должна" " быть позже начала!"
                ),
            ),
        ]
        default_related_name = "works"
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"
        ordering = ("company",)

    def __str__(self):
        return f"{self.employee.get_full_name()}" f'работал в "{self.company}"'
