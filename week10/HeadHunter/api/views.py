from django.http import JsonResponse
from django.shortcuts import render
from api.models import Company, Vacancy


# Create your views here.


def company_list(request):
    companies = Company.objects.all()
    companies_json = [c.to_json() for c in companies]

    return JsonResponse(companies_json, safe=False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(company.to_json())


def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    # select * from vacancies where company_id=<company.id>
    vacancies = company.vacancies.all()
    vacancies_json = [p.to_json() for p in vacancies]

    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(vacancy.to_json())


def vacancy_top10_list(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10:3]
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)
