# Generated by Django 4.1.1 on 2022-10-08 01:16

from django.db import migrations


def populate_status(apps, schemaeditor):
    entries = {
        "Customer":"A customer, can submit all the issues that he has.",
        "Agent":"An agent can move issues to many status.",
        "Manager":"A managet work as a agent, but h has a major rank"
    }
    Roles = apps.get_model("issues", "Roles")
    for name, desc in entries.items():
        status_obj = Roles(name=name, description=desc)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_roles_alter_issues_assignee_alter_issues_requester_and_more'),
    ]

    operations = [migrations.RunPython(populate_status)]