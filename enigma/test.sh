if [ $1 = "clear" ]; then
	rm *.out *.out2 plik2.png screen.out
else
	python enigma.py $1 $2 "test.bin" "test.out"
	python enigma.py $1 $2 "test.out" "test.out2"
	python enigma.py $1 $2 test2.bin test2.out
	python enigma.py $1 $2 test2.out test2.out2
	python enigma.py $1 $2 test3.bin test3.out
	python enigma.py $1 $2 test3.out test3.out2
	python enigma.py $1 $2 plik.png plik.out
	python enigma.py $1 $2 plik.out plik2.png
	python enigma.py $1 $2 screen.png screen.out
	python enigma.py $1 $2 screen.out screen2.out
fi
