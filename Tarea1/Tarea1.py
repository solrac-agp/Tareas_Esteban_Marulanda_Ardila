import funciones

#4. a)

Prob_a=funciones.Binomial(100,10)/2**100

print('La probabilidad de que la moneda salga 10 veces cara en 100 lanzamientos es',Prob_a)


#4. b)Asumire que es la probabilidad de que salga cara más de 30 veces en 100 lanzamientos. 
#Por otro lado, la propbabilidad de sacar cara más de 30 veces es sumar las probabilidades de sacar cara de 31 hasta 100, o bien
#uno menos la probabilidad de sacar cara desde 0 veces hasta 30; esto es combinar los números del cero hasta el 30 con 100 y sumarlos, o bien 2^30

print('La probabilidad de sacar cara más de 30 veces es',1-2**30/2*100)


