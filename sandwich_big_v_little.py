from sandwich_classes import Pool

initial_R0 = 10
initial_R1 = 10000

pool = Pool(initial_R0, initial_R1, .97)

# Small sandwich 
sandwich_in = 1
# amount_in, token_in, token_out
front_tx = (sandwich_in, 0, 0)
retail_tx = (3, 0, 0)

amount_out_front = pool.swap(front_tx[0], front_tx[1], front_tx[2])
back_tx = (amount_out_front, 1, 0)

amount_out_swap = pool.swap(retail_tx[0], retail_tx[1], retail_tx[2])

amount_out_back = pool.swap(back_tx[0], back_tx[1], back_tx[2])

print("Small sandwich token 0 gained: ", str(amount_out_back - sandwich_in))


pool.resetPool(initial_R0, initial_R1)


# Large sandwich
sandwich_in = 10000

front_tx = (sandwich_in, 0, 0)


amount_out_front = pool.swap(front_tx[0], front_tx[1], front_tx[2])
back_tx = (amount_out_front, 1, 0)

amount_out_swap = pool.swap(retail_tx[0], retail_tx[1], retail_tx[2])

amount_out_back = pool.swap(back_tx[0], back_tx[1], back_tx[2])

print("Large sandwich token 0 gained: ", str(amount_out_back - sandwich_in))
