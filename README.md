Como a base de que la fruta llegue sucia el codigo trabaja llamando en si misma a las clases para poder trabajar con ellas, aca entra la recursividad dentro del codigo así hasta llegar a que la fruta ya se vuelva comestible.

Recibe el estado "Sucia": Detecta que la fruta no se puede comer de inmediato y entra al bloque principal.

Hace la llamada interna ("Húmeda"): La función se llama a sí misma con la palabra "Húmeda". Como "Húmeda" llega directamente al caso de parada, imprime que se lavó con éxito y devuelve la confirmación. (Acá entra la recursividad)

Hace la llamada externa ("Limpia y Seca"): Con la lavada lista, ejecuta la segunda llamada a sí misma con "Limpia y Seca", alcanzando la última condición para confirmar que la fruta ya se puede comer.

Finaliza: Devuelve la respuesta final "Fruta perfecta para comer".
