class Solution:
    def validIPAddress(self, IP: str) -> str:
        isIp4 = self.checkIp4(IP)
        if isIp4:
            return "IPv4"
        isIp6 = self.checkIp6(IP)
        if isIp6:
            return "IPv6"
        return "Neither"
    def checkIp4(self, ip):
        ip = ip.split('.')
        if len(ip)!=4:
            return False
        for x in ip:
            if len(x)>1 and x[0]=='0':
                return False
            if len(x)>3 or len(x)==0:
                return False
            for i in x:
                try:
                    if int(i)>9 or int(i)<0:
                        return False
                except ValueError:
                    return False
            if int(x)>255 or int(x)<0:
                return False
        return True
    def checkIp6(self, ip):
        ip = ip.split(':')
        if len(ip) != 8:
            return False
        for x in ip:
            if len(x)>4 or len(x)==0:
                return False
            for i in x:
                try:
                    if int(i, 16)>15 or int(i, 16)<0:
                        return False
                except:
                    return False
        return True
        
# Runtime: 28 ms, faster than 68.11% of Python3 online submissions for Validate IP Address.
# Memory Usage: 14 MB, less than 20.02% of Python3 online submissions for Validate IP Address.
