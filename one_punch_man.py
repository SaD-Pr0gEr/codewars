class OnePunchMan:
    """
    Description
    You are Saitama (a.k.a. One Punch Man), and you are fighting against the monsters! You are strong enough to kill
    them with one punch, but after you punch 3 times, one of the remaining monsters will hit you once.
    Your health is health; number of monsters is monsters, damage that monster can give you is damage.

    Task
    Write a function that will calculate:
    how many hits you received, how much damage you received and your remaining health.
    if your health is <= 0, you die and function should return "hero died".
    Examples:
    kill_monsters(100, 3, 33); // => "hits: 0, damage: 0, health: 100"
    kill_monsters(50, 7, 10); // => "hits: 2, damage: 20, health: 30"
    """

    @staticmethod
    def my_case(health, monsters, damage):
        counter, hits, damage_sum = 0, 0, 0
        for i in range(monsters):
            if counter == 3:
                counter = 0
                health -= damage
                damage_sum += damage
                hits += 1
            counter += 1
        if health <= 0:
            return "hero died"
        return f"hits: {hits}, damage: {damage_sum}, health: {health}"

    @staticmethod
    def best_practice(dmg, monsters, hp):
        x, y = divmod(monsters, 3)
        hits = x - 1 + min(y, 1)
        return 'hero died' if dmg * hits >= hp else f'hits: {hits}, damage: {hits * dmg}, health: {hp - hits * dmg}'
