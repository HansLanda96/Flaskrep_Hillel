from datetime import datetime, time


def current_time():
    """Returns the current time in a readable format with params for the clock"""
    while True:
        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        if time(8, 0) <= datetime.now().time() <= time(18, 0):
            return f'<h2>Greetings traveller! Site is working!</h2><h3>{dt}</h3>'
        else:
            return f'<h2>Good evening traveller! Site is working, but no one will answer your question!</h2>' \
                   f'<h3>{dt}</h3>'


def average_height_weight():
    """Returns the average height and weight of the users from file"""
    user = {}
    with open('hw.csv', 'r') as f:
        next(f)
        for line in f:
            ind, height, weight = line.split(',')
            user[ind] = [float(height), float(weight)]
    avg_height = round((sum(user[ind][0] for ind in user) * 2.54) / len(user), 2)  # [0] index
    avg_weight = round((sum(user[ind][1] for ind in user) / 2.2046) / len(user), 2)  # [1] index
    return avg_height, avg_weight


def show_requirements():
    """Returns the requirements for the project"""
    req = []
    with open('requirements.txt', 'r') as f:
        for line in f:
            req.append(line.strip())
    return '<br>'.join(req)
