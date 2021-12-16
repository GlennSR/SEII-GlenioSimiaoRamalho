#include<stdio.h>

float carga = 100.0;

float carregar(float tempo)
{
	carga += tempo*2;
	return carga;
}

float descarregar(float taxa, float tempo)
{
	carga -= taxa*tempo;
	return carga;
}

float ler_carga()
{
	return carga;
}


