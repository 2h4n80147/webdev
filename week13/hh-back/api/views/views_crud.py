import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Company, Vacancy


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [c.to_json() for c in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)

        company = Company.objects.create(name=data.get('name'))

        return JsonResponse(company.to_json())


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(company.to_json())

    elif request.method == 'PUT':
        data = json.loads(request.body)

        company.name = data.get('name', company.name)
        company.save()

        return JsonResponse(company.to_json())

    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})



@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [c.to_json() for c in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)

        # option 1
        # vacancy = vacancy(name=data['name'])
        # vacancy.save()

        # option 2
        vacancy = Vacancy.objects.create(name=data.get('name'))

        return JsonResponse(vacancy.to_json())


@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())

    elif request.method == 'PUT':
        data = json.loads(request.body)

        vacancy.name = data.get('name', vacancy.name)
        vacancy.save()

        return JsonResponse(vacancy.to_json())

    elif request.method == 'DELETE':
        vacancy.delete()

        return JsonResponse({'deleted': True})
