import base64

def string_to_base64(input_string):
    # 将输入字符串转换为字节
    byte_data = input_string.encode('utf-8')
    # 进行Base64编码
    base64_encoded = base64.b64encode(byte_data)
    # 将编码后的字节转换回字符串
    return base64_encoded.decode('utf-8')

def base64_to_string(base64_string):
    # 将Base64编码的字符串解码为字节
    byte_data = base64.b64decode(base64_string)

    # 将字节转换回UTF-8格式的字符串
    original_string = byte_data.decode('utf-8')

    return original_string


# 示例
input_string = input('base64编码前的字符串:')
encoded_string = string_to_base64(input_string)
print("Base64编码后的字符串:", encoded_string,end = '\n\n')

encoded_string = 'SGVsbG8gV29ybGQ='
decoded_string = base64_to_string(encoded_string)
print("Base64编码的字符串: ", encoded_string)
print("解码后的原始字符串: ", decoded_string)
