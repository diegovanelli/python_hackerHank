
def pageCount(n, p):# Quantidade de páginas viradas a partir do início do livro
  viradas_inicio = p // 2

  # Quantidade de páginas viradas a partir do final do livro
  print(n // 2)
  viradas_final = (n // 2) - (p // 2)

  # Retornar a menor quantidade de páginas viradas
  return min(viradas_inicio, viradas_final)
    
    

if __name__ == '__main__':
  n = 20
  p = 4

  result = pageCount(n, p)

  print(result)
