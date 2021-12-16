#include<stdio.h>

float gasolina = 50.0;

float encher(float quantidade)
{
	gasolina += quantidade;
	return gasolina;
}

float secar(float km_por_litro, float km_rodados)
{
	gasolina -= km_rodados/km_por_litro;
	return gasolina;
}

float ler_gasolina()
{
	return gasolina;
}
