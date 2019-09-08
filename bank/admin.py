from django.contrib import admin

from bank.models import Branch, Bank


class BranchInline(admin.TabularInline):
    model = Branch
    extra = 1


class BankAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'name',
        'id',
    )
    inlines = (
        BranchInline,
    )


admin.site.register(Bank, BankAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = (
        'state',
        'city',
        'district',
        'bank',
        'branch',
        'ifsc',
    )

    search_fields = (
        'state',
        'city',
        'district',
        'ifsc',
        'branch',
        'bank__name',
        'address',
    )

    def get_queryset(self, request):
        return super(
                BranchAdmin, self
        ).get_queryset(
                request
        ).prefetch_related('bank')


admin.site.register(Branch, BranchAdmin)
