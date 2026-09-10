nome = input ("Nome do aluno: ")
diciplina = input ("Nome da disciplina: ")
nota1 = float(input ("Digite sua primeira nota:"))
nota2 =float(input ("Digite sua segunda nota:"))
nota3 = float(input ("Digite sua terceira nota:"))  

media = (nota1 + nota2 + nota3) / 3

print("Nome do aluno:", nome)
print("Disciplina:", diciplina)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print(f"Média final: {media:.2f}")  # Exibe a média com duas casas recebaaa sabedoriaaa