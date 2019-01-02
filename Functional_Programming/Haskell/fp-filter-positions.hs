f :: [Int] -> [Int]
f (_ : y : ys) = y : f ys
f _ = []

main = do
  inputdata <- getContents
  mapM_ (putStrLn. show). f. map read. lines $ inputdata

