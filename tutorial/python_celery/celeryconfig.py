broker_url = 'redis://localhost:6379/0' # for redis
#broker_url = 'pyamqp://' # for rabbitmq 
result_backend = 'rpc://'
result_persistent = True
task_routes = {
    'add_module.tasks.add': {'queue':'add'},
    'mat_mul_module.tasks.mat_mul': {'queue':'mat_mul'},
    'factorial_module.tasks.factorial': {'queue':'factorial'}
}
