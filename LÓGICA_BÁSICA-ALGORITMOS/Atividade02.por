programa {
	funcao inicio() {
	//Faça um programa que calcule o consumo médio de um automóvel. 
    //Para isso é necessário a distância total percorrida pelo automóvel e o total de combustível gasto. 
    //Obs:distância/combustível.	
	
	real consumo_medio, distancia_total, total_combustivel_gasto
	
	escreva("Distância total percorrida:")
    leia(distancia_total)

    escreva("Total de combustível gasto:" )
    leia(total_combustivel_gasto)
	
	consumo_medio = distancia_total / total_combustivel_gasto
    escreva(consumo_medio)

	}
}
