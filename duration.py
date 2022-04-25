class Duration:

    @staticmethod
    def my_shit_case(seconds):
        if seconds < 60:
            return f"{seconds} second"
        minute = seconds // 60
        second = seconds % 60 if seconds % 60 != 0 else 0
        hour = 0
        day = 0
        year = 0
        while second >= 60:
            second -= 60
            minute += 1
        while minute >= 60:
            minute -= 60
            hour += 1
        while hour >= 24:
            hour -= 24
            day += 1
        while day >= 360:
            day -= 360
            year += 1
        if year:
            if day:
                if hour:
                    if minute:
                        if second:
                            return f"{year} year, {day} days, {hour} hours, {minute} minutes, {second} seconds"
                        else:
                            return f"{year} year, {day} days, {hour} hours, {minute} minutes"
                    else:
                        return f"{year} year, {day} days, {hour} hours"
                else:
                    return f"{year} year, {day} days"
            else:
                return f"{year} year"
        else:
            if day:
                if hour:
                    if minute:
                        if second:
                            return f"{day} days, {hour} hours, {minute} minutes, {second} seconds"
                        else:
                            return f"{hour} hours, {minute} minutes"
                    else:
                        return f"{hour} hours"
                else:
                    return f"{day} days"
            else:
                if hour:
                    if minute:
                        if second:
                            return f"{hour} hours, {minute} minutes, {second} seconds"
                        else:
                            return f"{hour} hours, {minute} minutes"
                    else:
                        return f"{hour} hours"
                else:
                    if minute:
                        if second:
                            return f"{minute} minutes, {second} seconds"
                        else:
                            return f"{minute} minutes"
                    else:
                        return f"{second} seconds"

    @staticmethod
    def best_practice_pluralize(n, word):
        if n == 1:
            return '%d %s' % (n, word)
        return '%d %ss' % (n, word)

    def format_duration(self, seconds):
        if seconds == 0:
            return "now"

        ONE_MINUTE = 60
        ONE_HOUR = 60 * ONE_MINUTE
        ONE_DAY = 24 * ONE_HOUR
        ONE_YEAR = 365 * ONE_DAY

        units = (
            (ONE_YEAR, 'year'),
            (ONE_DAY, 'day'),
            (ONE_HOUR, 'hour'),
            (ONE_MINUTE, 'minute'),
            (1, 'second'),
        )

        r = []
        for unit in units:
            time_period, word = unit
            if seconds >= time_period:
                n = int(seconds / time_period)
                r.append(self.best_practice_pluralize(n, word))
                seconds -= n * time_period


print(Duration().my_shit_case(16000))
