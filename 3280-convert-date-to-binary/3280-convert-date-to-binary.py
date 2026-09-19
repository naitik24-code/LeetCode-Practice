class Solution(object):
    def convertDateToBinary(self, date):
        year,month,day=date.split("-")
        year=bin(int(year))[2:]
        month=bin(int(month))[2:]
        day=bin(int(day))[2:]
        return year+"-"+month+"-"+day
        