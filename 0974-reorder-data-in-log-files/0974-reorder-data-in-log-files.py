class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            if log.split()[-1].isdigit():
                digit_logs.append(log)

            else:
                letter_logs.append(log)

        #sort letter_logs with primary_key as the content and secondary key as the identifier
        letter_logs.sort(key=lambda x: (x.split(" ",1)[1], x.split()[0]))

        return letter_logs + digit_logs
