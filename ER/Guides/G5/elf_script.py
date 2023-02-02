import lief
import sys

filename = sys.argv[1]
binary  = lief.parse(filename)

print("Type: ", binary.header.file_type)
print("Architecture: ", binary.header.machine_type)
print("Libraries: ",binary.libraries)

print("Compiler: ", str(binary.concrete.get_section(".comment").content,'utf8'))

print("Dynamic symbols:")
for ds in binary.concrete.dynamic_symbols:
    print(ds)

print("Entrypoint: ", binary.entrypoint, "->" ,hex(binary.entrypoint))

relro = "None"
if binary.concrete.get(lief.ELF.SEGMENT_TYPES.GNU_RELRO):
    relro = "Partial RELRO"
    if "BIND_NOW" in str(binary.concrete.get(lief.ELF.DYNAMIC_TAGS.FLAGS)):
        relro = "Full RELRO"

print("RELRO: ", relro)

print("PIE: ", binary.is_pie)

print("Canaries: ", "True" if (binary.concrete.get_symbol("__stack_chk_fail") or binary.concrete.get_symbol("__stack_chk_guard" or binary.concrete.get_symbol("__intel_security_cookie"))) else "False")

stripped = "True" if len(binary.concrete.static_symbols) == 0 else "False"

print("Stripped: ", stripped)
