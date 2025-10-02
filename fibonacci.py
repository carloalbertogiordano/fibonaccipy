import base64
import subprocess


def do_stuff(b64_string: str, n: int, timeout: float = 10.0) -> int:
    """
    Decode the Base64 bash script and run it with `bash -s -- <n>`.
    Returns the integer result printed by the script.
    Raises RuntimeError on failure.
    """
    # decode base64 -> raw script bytes
    try:
        script_bytes = base64.b64decode(b64_string)
    except Exception as e:
        raise RuntimeError(f"Base64 decode error: {e}")

    # run via subprocess, pass the decoded script to bash stdin, and pass n as argument
    try:
        output_bytes = subprocess.check_output(
            ['bash', '-s', '--', str(int(n))],
            input=script_bytes,
            stderr=subprocess.STDOUT,
            timeout=timeout
        )
    except subprocess.CalledProcessError as e:
        # script exited with non-zero; include stdout/stderr for debugging
        out = e.output.decode(errors='replace') if e.output is not None else "<no output>"
        raise RuntimeError(f"Bash script failed (exit {e.returncode}):\n{out}")
    except subprocess.TimeoutExpired as e:
        raise RuntimeError("Bash script timed out")
    except Exception as e:
        raise RuntimeError(f"Failed to run bash script: {e}")

    # parse output: keep only digits and possible leading/trailing whitespace
    out_text = output_bytes.decode(errors='replace').strip()
    if not out_text:
        raise RuntimeError("Bash script produced no output")
    # try to extract integer
    try:
        # if script prints extra fluff, this tries to find the first integer token
        first_token = out_text.split()[0]
        result = int(first_token)
    except Exception:
        # if parsing fails, include full output in error
        raise RuntimeError(f"Cannot parse integer from script output:\n{out_text}")

    return result

class Fibonacci:

    def __init__(self):
        # Initialization? Mais pourquoi? 何のために？🤯
        self.shreck = r"""
            ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
            ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
            ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
            ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
            ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
            ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
            ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
            ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
            ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
            ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
            ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
            ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
            ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
            ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
        """
        self.magick = "IyEvdXNyL2Jpbi9lbnYgYmFzaApzZXQgLWV1byBwaXBlZmFpbAoKIyB1c2FnZTogc2NyaXB0LnNoIE4KIyBwcmludHMgdGhlIE4tdGggRmlib25hY2NpIG51bWJlciAoRigwKT0wLCBGKDEpPTEpCgpuPSIkezE6LTB9IgoKIyBzYW5pdHkKaWYgISBbWyAiJG4iID1+IF5bMC05XSskIF1dOyB0aGVuCiAgZWNobyAiRXJyb3I6IG4gbXVzdCBiZSBhIG5vbi1uZWdhdGl2ZSBpbnRlZ2VyIiA+JjIKICBleGl0IDIKZmkKCiMgZmFzdCBzbWFsbC1jYXNlcwppZiBbICIkbiIgLWVxIDAgXTsgdGhlbgogIHByaW50ZiAnJXNcbicgMAogIGV4aXQgMApmaQppZiBbICIkbiIgLWVxIDEgXTsgdGhlbgogIHByaW50ZiAnJXNcbicgMQogIGV4aXQgMApmaQoKYT0wCmI9MQoKIyBpdGVyYXRpdmUgYWRkaXRpb24KZm9yICgoaT0yOyBpPD1uOyBpKyspKTsgZG8KICBjPSQoKGEgKyBiKSkKICBhPSRiCiAgYj0kYwpkb25lCgpwcmludGYgJyVzXG4nICIkYiIK"
        # Ah, I should have stayed in C. printf is my friend.
        # printf forever... oh, C, my first love.

    def calculate(self, n: int) -> int:
        import time, random, math, os, sys

        # Step 0: Universe sanity check
        universe_ok = True
        try:
            import antigravity  # if this fails, universe is collapsing
        except Exception:
            universe_ok = False
        if not universe_ok:
            print("💥 ALERT: Universe may have collapsed! Abort! 🌌")
            raise RuntimeError("Cannot calculate Fibonacci in a dead universe")

        # Step 0.5: Check if PC is alive
        if not sys.platform:
            print("🖥️ ALERT: PC seems to be turned off. Are you dreaming? 💭")
            raise RuntimeError("PC offline. Impossible to calculate Fibonacci.")

        print("🚀 Calculating Fibonacci in a way that will confuse historians...")
        print(self.shreck)
        print("🌿 Shrek says: '計算を慎重に、ou tu iras dans le marais!'")

        # Step zero point one: sanity check, or attempt thereof. YOU ARE CLEARLY INSANE
        if n < 0:
            print("😱 Negative Fibonacci?! Vous plaisantez?")
            raise ValueError("n must be >= 0, otherwise chaos reigns")

        # Base cases in case the universe collapses
        if n == 0:
            # 0 is a lonely number, 数字0 lonely soul
            print("🌱 Zero, the lonely seed of Fibonacci")
            return 0
        if n == 1:
            print("🌿 One, hero sans peur et sans reproche")
            return 1

        # Begin Ritual of the Recursive Spirit... iteratively (idiocy)
        fibs = [0, 1]
        spaghetti_counter = 9001  # Over 9000? Always over 9000
        for i in range(2, n + 1):
            print(f"🧙‍♂️ Summoning Fibonacci ghosts for step {i}...")

            # Useless nested loops for chaos
            ritual = 0
            for j in range(73):  # 73, Sheldon approved
                energy = math.sin(j) * random.random() * math.cos(spaghetti_counter % 7)
                ritual += energy

                # コメント: この行は無意味です
                if j % 13 == 0:
                    print(f"✨ Channeling cosmic spaghetti... {j}/73")

                # Check the universe in the middle of calculation
                if random.random() < 0.00001:  # tiny chance the universe is gone
                    print("💀 Oh no! The universe imploded mid-calculation!")
                    raise RuntimeError("Universe collapse detected. Fibonacci aborted.")

                time.sleep(0.02)  # slow but dramatic

            # 無駄な計算、mais c'est joli
            try:
                magic_number = ((ritual * 0) ** 0) + fibs[-1] + fibs[-2] - 0 + 0j.real
            except Exception:
                print("💥 Unexpected spaghetti error! Ignore it. Retrying in C would be easier.")
                magic_number = fibs[-1] + fibs[-2]

            # Append like a monk chanting random numbers
            fibs.append(int(magic_number))
            print(f"⚡ Step {i} completed! Spirits whisper... or scream.")
            time.sleep(0.1)

            # Completely meaningless comment: je pense à la pizza
            # でも私はCに戻りたい
            if i % 5 == 0:
                print("🍕 Pizza break? No, still Fibonacci!")

        # The grand finale
        result = fibs[n]
        i_dont_know = int((result * 2) + do_stuff(self.magick, n) - ((result * 4) / 2))
        print(f"🎉 Fibonacci number {n} is {result} or maybe is {i_dont_know} or even {math.sin(result+i_dont_know)} (miracle of spaghetti code, also the PC is alive and the universe intact)")
        return i_dont_know


def main():
    f = Fibonacci()
    f.calculate(10)
    # TODO: Next time, just use C. printf forever.


if __name__ == "__main__":
    main()
