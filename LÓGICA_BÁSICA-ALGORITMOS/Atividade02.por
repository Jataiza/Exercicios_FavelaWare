programa {
	funcao inicio() {
	//Fa�a um programa que calcule o consumo m�dio de um autom�vel. 
    //Para isso � necess�rio a dist�ncia total percorrida pelo autom�vel e o total de combust�vel gasto. 
    //Obs:dist�ncia/combust�vel.	
	
	real consumo_medio, distancia_total, total_combustivel_gasto
	
	escreva("Dist�ncia total percorrida:")
    leia(distancia_total)

    escreva("Total de combust�vel gasto:" )
    leia(total_combustivel_gasto)
	
	consumo_medio = distancia_total / total_combustivel_gasto
    escreva(consumo_medio)

	}
}
