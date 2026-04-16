from pathlib import Path


class PID:
    def __init__(self, kp, ki, kd, setpoint, dt):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.dt = dt
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, measured):
        error = self.setpoint - measured
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative


def simulate():
    target = 100.0
    current = 0.0
    dt = 0.1
    pid = PID(kp=0.35, ki=0.02, kd=0.08, setpoint=target, dt=dt)

    rows = ["step,target,current,error,control"]

    for step in range(1, 81):
        control = pid.update(current)

        # A tiny fake plant: the system moves only part of the commanded amount.
        current += control * 0.05

        error = target - current
        rows.append(f"{step},{target:.2f},{current:.4f},{error:.4f},{control:.4f}")

        if step in [1, 2, 3, 5, 10, 20, 40, 80]:
            print(
                f"step={step:02d} target={target:.1f} "
                f"current={current:.2f} error={error:.2f} control={control:.2f}"
            )

    output_dir = Path(__file__).resolve().parents[1] / "outputs"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "task01_pid_demo_result.csv"
    output_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"\nSaved result to: {output_path}")


if __name__ == "__main__":
    simulate()

