number_of_completed_tasks = 12
number_of_hours_spent = 1.5
course = 'Python'
time_per_task = number_of_hours_spent / number_of_completed_tasks
print('Курс:', course, 'всего задач:', number_of_completed_tasks,
      'затрачено часов:', number_of_hours_spent, 'среднее время выполнения:',
      round(time_per_task, 3), 'часа')
