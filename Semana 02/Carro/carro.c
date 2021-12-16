#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "bateria.h"
#include "tanque.h"

void som(float tempo)
{
	float taxa = 0.5;
	float carga = descarregar(taxa, tempo);
	printf("A carga da bateria eh de %.2f porcento\n", carga);
}

void gasto_de_gasolina(float km_por_litro, float km_rodados)
{
	float gasolina = secar(km_por_litro, km_rodados);
	printf("O estado do tanque de combustivel apos rodar %.1f km eh de %.2f litros\n", km_rodados, gasolina);
}

int main()
{
	char marca[] = "Honda";
	char modelo[] = "Civic";
	float km_por_litro = 10.0;
	float tempo, km_rodados;
	
	printf("Marca do veiculo: %s \nModelo: %s \nKm/l: %.1f \nCarga atual da bateria: %0.2f \nEstado do Tanque de Combustivel: %.2f\n\n", marca, modelo, km_por_litro, ler_carga(), ler_gasolina());
	
	printf("Digite quantas horas o som ficou ligado: ");
  	scanf("%f", &tempo);

	printf("Digite quantos km foram rodados: ");
	scanf("%f", &km_rodados);
  	
  	som(tempo);
	gasto_de_gasolina(km_por_litro, km_rodados);
}


