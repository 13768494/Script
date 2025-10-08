from Crypto.Hash import MD4
import itertools

# 生成NTLM哈希的函数
def generate_ntlm_hash(password):
    """使用MD4算法生成NTLM哈希"""
    md4_hash = MD4.new()
    md4_hash.update(password.encode('utf-16le'))
    return md4_hash.hexdigest().upper()

# 暴力破解NTLM哈希的函数
def brute_force_ntlm_hash(target_hash):
    """暴力破解NTLM哈希，假设密码是8位或以下数字组成"""
    charset = '0123456789'  # 数字字符集
    for length in range(1, 9):  # 假设密码长度为1到8个字符
        for password_tuple in itertools.product(charset, repeat=length):
            password = ''.join(password_tuple)
            calculated_hash = generate_ntlm_hash(password)
            print(f"尝试密码: {password} -> 哈希值: {calculated_hash}")
            if calculated_hash == target_hash:
                return password
    return None

# 目标NTLM哈希
target_hash = "F4AD50F57683D4260DFD48AA351A17A8"

# 调用暴力破解函数
found_password = brute_force_ntlm_hash(target_hash)

if found_password:
    print(f"成功破解密码: {found_password}")
else:
    print("没有找到密码。")