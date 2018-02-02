from django.db import models

class Aluno(models.Model):
	class Meta: 
		verbose_name_plural='Alunos' 
		verbose_name='Aluno' 
		db_table='tbAluno'

        id=models.CharField(verbose_name='id', db_column="idAluno",max_length=100, primary_key=True)
        nome=models.CharField(verbose_name='nome', db_column="NomeAluno",max_length=100)

	def __unicode__(self):
		return '%s' % (self.nome) 		