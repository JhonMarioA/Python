# Product
class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.os = None

    def __str__(self):
        return (f"Computer: CPU={self.cpu}, GPU={self.gpu}, RAM={self.ram}, "
                f"Storage={self.storage}, OS={self.os}")
                

# Builder
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def install_os(self, os):
        self.computer.os = os
        return self

    def build(self):
        return self.computer


# Director (opcional, para crear configuraciones predefinidas)
class Director:
    @staticmethod
    def build_gaming_pc():
        return (ComputerBuilder()
                .set_cpu("AMD Ryzen 9 7900X")
                .set_gpu("NVIDIA RTX 4080")
                .set_ram("32GB DDR5")
                .set_storage("2TB NVMe SSD")
                .install_os("Windows 11 Pro")
                .build())

    @staticmethod
    def build_office_pc():
        return (ComputerBuilder()
                .set_cpu("Intel i5 12400")
                .set_ram("16GB DDR4")
                .set_storage("512GB SSD")
                .install_os("Windows 10 Home")
                .build())

    @staticmethod
    def build_linux_server():
        return (ComputerBuilder()
                .set_cpu("AMD EPYC 7763")
                .set_ram("64GB ECC")
                .set_storage("4TB SSD RAID")
                .install_os("Ubuntu Server 22.04")
                .build())


# Uso
gaming_pc = Director.build_gaming_pc()
office_pc = Director.build_office_pc()
server = Director.build_linux_server()

print(gaming_pc)
print(office_pc)
print(server)
