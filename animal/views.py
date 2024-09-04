"""views for serializer models."""

from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response

# from datetime import timedelta, timezone
# from collections import defaultdict
from rest_framework import status

from rest_framework import viewsets
from .serializers import (
    AnimalBaseSerializer,
    PurchasedAnimalSerializer,
    LocallyServicedAnimalSerializer,
    MedicineTreatmentSerializer,
    DosageTreatmentSerializer,
    # ServicingSerializer,
    DisposalSerializer,
    # MilkProductionSerializer,
)
from .models import (
    AnimalBase,
    PurchasedAnimal,
    LocallyServicedAnimal,
    MedicineTreatment,
    DosageTreatment,
    # Servicing,
    Disposal,
    # MilkProduction,
)


# class ServicingViewSet(viewsets.ModelViewSet):
#     queryset = Servicing.objects.all()
#     serializer_class = ServicingSerializer


class PurchasedViewSet(viewsets.ModelViewSet):
    queryset = PurchasedAnimal.objects.all()
    serializer_class = PurchasedAnimalSerializer


class LocallyServicedViewSet(viewsets.ModelViewSet):
    queryset = LocallyServicedAnimal.objects.all()
    serializer_class = LocallyServicedAnimalSerializer


class MedicineTreatmentViewSet(viewsets.ModelViewSet):
    queryset = MedicineTreatment.objects.all()
    serializer_class = MedicineTreatmentSerializer


class DosageTreatmentViewSet(viewsets.ModelViewSet):
    queryset = DosageTreatment.objects.all()
    serializer_class = DosageTreatmentSerializer


class AnimalBaseViewSet(viewsets.ModelViewSet):
    queryset = AnimalBase.objects.all()
    serializer_class = AnimalBaseSerializer

    def get_query(self):
        queryset = super().get_queryset()
        gender = self.request.query_params.get("gender")

        if gender:
            queryset = queryset.filter(gender=gender)
        return queryset


class DisposalViewSet(viewsets.ModelViewSet):
    queryset = Disposal.objects.all()
    serializer_class = DisposalSerializer


# class MilkProductionView(viewsets.ViewSet):
#     def list(self, request):
#         animal_id = request.query_params.get("animal_id")
#         date = request.query_params.get("date")
#         start_date = request.query_params.get("start_date")
#         end_date = request.query_params.get("end_date")
#         year = request.query_params.get("year")
#         month = request.query_params.get("month")

#         if animal_id and date:
#             # Daily production
#             try:
#                 record = MilkProduction.objects.get(
#                     animal_id=animal_id, date_of_production=date
#                 )
#                 serializer = MilkProductionSerializer(record)
#                 return Response(serializer.data)
#             except MilkProduction.DoesNotExist:
#                 return Response(
#                     {"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND
#                 )

#         elif animal_id and start_date and end_date:
#             # Production in range
#             records = MilkProduction.objects.filter(
#                 animal_id=animal_id, date_of_production__range=[start_date, end_date]
#             ).order_by("date_of_production")
#             serializer = MilkProductionSerializer(records, many=True)
#             return Response(serializer.data)

#         elif animal_id and not (start_date or end_date):
#             # Weekly and monthly totals
#             today = timezone.now().date()
#             start_of_week = today - timedelta(days=today.weekday())
#             start_of_month = today.replace(day=1)

#             weekly_records = MilkProduction.objects.filter(
#                 animal_id=animal_id, date_of_production__range=[start_of_week, today]
#             ).order_by("date_of_production")
#             monthly_records = MilkProduction.objects.filter(
#                 animal_id=animal_id, date_of_production__range=[start_of_month, today]
#             ).order_by("date_of_production")

#             weekly_total = sum(record.total_daily_quantity for record in weekly_records)
#             monthly_total = sum(
#                 record.total_daily_quantity for record in monthly_records
#             )

#             return Response(
#                 {
#                     "weekly_total": weekly_total,
#                     "monthly_total": monthly_total,
#                 }
#             )

#         elif animal_id and year and month:
#             # Display monthly production
#             productions = MilkProduction.objects.filter(
#                 animal_id=animal_id,
#                 date_of_production__year=year,
#                 date_of_production__month=month,
#             ).order_by("date_of_production")
#             daily_totals = []
#             weekly_totals = defaultdict(float)
#             monthly_totals = 0

#             for production in productions:
#                 date = production.date_of_production
#                 total_daily = production.total_daily_quantity
#                 daily_totals.append(
#                     {
#                         "date": date,
#                         "morning_quantity": production.morning_quantity,
#                         "evening_quantity": production.evening_quantity,
#                         "total_daily": total_daily,
#                     }
#                 )

#                 week_number = date.isocalendar()[1]
#                 weekly_totals[week_number] += total_daily
#                 monthly_totals += total_daily

#             return Response(
#                 {
#                     "daily_totals": daily_totals,
#                     "weekly_totals": weekly_totals,
#                     "monthly_total": monthly_totals,
#                 }
#             )

#         else:
#             return Response(
#                 {"detail": "Invalid query parameters."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )


class GenderDistributionView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            gender_counts = AnimalBase.objects.values("gender").annotate(
                count=Count("gender")
            )
            data = {"male": 0, "female": 0}
            for entry in gender_counts:
                if entry["gender"] == "M":
                    data["male"] = entry["count"]
                elif entry["gender"] == "F":
                    data["female"] = entry["count"]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
