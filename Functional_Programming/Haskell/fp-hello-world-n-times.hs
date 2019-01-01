hello_world :: Int -> IO ()
hello_world n = sequence_ [putStrLn "Hello World" | _ <- [1..n]]

main :: IO ()
main = do
  n <- readLn :: IO Int
  hello_world n

