solveMeFirst :: Int -> Int -> Int
solveMeFirst a b = a + b

main = do
  x <- readLn
  y <- readLn
  let z = solveMeFirst x y in
    print z

