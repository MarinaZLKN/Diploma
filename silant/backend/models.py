from django.db import models


# Техническая модель
class TechnicalModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Модель трансмиссии
class TransmissionModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Модель двигетеля
class EngineModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Модель управляемого моста
class ControlledBridgeModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Модель ведущего моста
class DrivingBridgeModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Тип технического обслуживания
class TypeOfMaintenance(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Метод восстановления
class RecoveryMethod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Клиент
class Client(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class FailureNode(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Сервисная компания
class ServiceCompany(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


# Машина
class Machine(models.Model):
    machine_factory_number = models.CharField(max_length=4)
    engine_factory_number = models.CharField(max_length=100)
    transmission_factory_number = models.CharField(max_length=100)
    driving_bridge_factory_number = models.CharField(max_length=100)  # Зав. номер ведущего моста
    controlled_bridge_factory_number = models.CharField(max_length=100)  # Зав. номер управляемого моста
    delivery_contract = models.CharField(max_length=100)  # Договор поставки номера, дата
    shipment_date = models.DateField()  # дата отгрузки с завода
    consignee = models.CharField(max_length=100)  # грузополучатель
    delivery_address = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)  # комплектация

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)
    engine_model = models.ForeignKey(EngineModel, on_delete=models.CASCADE)
    technical_model = models.ForeignKey(TechnicalModel, on_delete=models.CASCADE)
    transmission_model = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE)
    driving_bridge_model = models.ForeignKey(DrivingBridgeModel, on_delete=models.CASCADE)
    controlled_bridge_model = models.ForeignKey(ControlledBridgeModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.machine_factory_number


# ТО
class Maintenance(models.Model):
    date_of_maintenance = models.DateField()  # дата ТО
    operating_time = models.IntegerField()  # наработка, м/час
    order_number = models.CharField(max_length=100)  # номер заказ-наряда
    data_of_order = models.DateField()  # дата заказ-наряда

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)  # Организация, проводившая ТО
    type_of_maintenance = models.ForeignKey(TypeOfMaintenance, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)


# Рекламации
class Claim(models.Model):
    date_of_failure = models.DateField()  # дата отказа
    operating_time = models.IntegerField()  # наработка, м/час
    spare_parts_used = models.TextField(null=True, blank=True, default=None)  # используемые запасные части
    date_of_recovery = models.DateField()  # дата восстановления
    technical_downtime = models.IntegerField(default=None)  # время простоя техники
    description_of_failure = models.CharField(max_length=100)  # Описание отказа

    failure_node = models.ForeignKey(FailureNode, on_delete=models.CASCADE)  # узел отказа
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)

    # по сути, дата восстановления - дата отказа
    def downtime(self):
        self.technical_downtime = (self.date_of_recovery - self.date_of_failure).days
        self.save()

