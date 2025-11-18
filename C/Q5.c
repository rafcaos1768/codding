//resolução da q5 de uma maneira diferente !!!

int index=0; int tamanho; int indexTamanho; 
  char buffer[20];char inverso[20];  
 
 //transformar o numero em string para contar as casas
  sprintf(buffer, "%d", num);
  tamanho = strlen(buffer); 
  indexTamanho = tamanho; 
  //passar a string para a outra string 

  while(index != tamanho){
    inverso[index] = buffer[indexTamanho-1];

    indexTamanho --;
    index++; 
  }

  inverso[tamanho] = '\0'; 
  num = atoi(inverso);
