nome = input ("Nome aluno: ")
diciplina= input ("Disciplina:")
nota1 = float (input ("Digite primeiera nota:"))
nota2 = float (input ("Digite segunda nota:"))
nota3 = float(input ("Digite terceita nota :"))

media = (nota1 + nota2 + nota3) /3

print("Nome do aluno:", nome)
print("Disciplina:", diciplina)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print(f"Média final: {media:.2f}")  # Exibe a média com duas casas decimais

if media >= 6:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")



