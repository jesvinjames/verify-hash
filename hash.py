import hashlib
f = open("C:/Users/user/Downloads/pop-os_amd64_intel_45.iso", 'rb')
file_hash = "a2dd27d600e0d9f7e93ef93f2da2704d9eda63dfb3bfbd849feafb3511c11b8f"
print(hashlib.sha256(f.read()).hexdigest() == file_hash)
    
