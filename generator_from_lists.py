worker_names = 'Jhon', 'Eddy', 'Max'
worker_volumes = 1000, 10000, 100_000
worker_premium = '10.25', '20.25', '15.5%'


def create_dict_from_lists(names: list[str], volumes: list[int], premium: list[str]) -> dict[str, float]:
    new_dict = {name: volumes * float(premium.strip('%')) / 100 for name, volumes, premium in
                zip(names, volumes, premium)}
    yield new_dict


print(*create_dict_from_lists(worker_names, worker_volumes, worker_premium))
