from django.db import models


class Bank(models.Model):
    """
    Contains name of the bank and its ID
    db_table = 'banks' is used from Postgres

    """

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, help_text="Name of the bank")

    class Meta:
        db_table = 'bank'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Branch(models.Model):
    """
    Contains branch information of the Bank.
    A Bank has many branches : ManyToOne Rel to Bank

    """
    ifsc = models.CharField(primary_key=True, max_length=11,
                            help_text="IFSC code of branch")

    bank = models.ForeignKey(Bank, help_text="FK to Bank table")

    branch = models.CharField(max_length=127, help_text="Area of the branch is located")

    address = models.CharField(max_length=195, help_text="Detailed address of the branch")

    city = models.CharField(max_length=50, help_text="City where branch is located")

    district = models.CharField(max_length=50, help_text="District where branch is located")

    state = models.CharField(max_length=26, help_text="State in which branch is located")

    class Meta:
        db_table = 'branch'
        verbose_name_plural = 'Branches'
        ordering = ['state', 'city', 'district', 'branch']

    def __unicode__(self):
        return 'IFSC: {}, Bank:{}, Branch'.format(self.ifsc, self.bank, self.branch)

    @property
    def bank_name(self):
        return self.bank.name
