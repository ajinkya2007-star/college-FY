"""
GREENTECH - Tkinter Desktop Interface
Converted from the original console program: same logic, same e-waste data,
same tips, now presented as a GUI with tabs instead of a text menu.
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ----------------------------------------------------------------------
# Data (identical to the console version)
# ----------------------------------------------------------------------
E_WASTE_DATA = {
    "samsung": {
        "s": {
            "common_issues": "Battery degradation, screen damage, and software issues.",
            "repair_advice": "Visit an authorized service center for battery or screen replacement.",
            "reuse_donation": "Use the device as a media player or donate it if working.",
            "recycling": "Give the device to an authorized e-waste recycler.",
            "safety": "Do not use a swollen battery or damaged charger.",
            "data_wiping": "Back up data and perform a factory reset before disposal.",
            "environmental_impact": "Improper disposal can release harmful materials and waste valuable resources.",
            "resale": "Estimated resale depends on model, age, condition, and battery health.",
        },
        "a": {
            "common_issues": "Battery wear, charging problems, and screen damage.",
            "repair_advice": "Check the charger and consult a service professional for repairs.",
            "reuse_donation": "Use it for learning, music, or donate it to someone in need.",
            "recycling": "Recycle through an authorized e-waste collection center.",
            "safety": "Avoid damaged batteries and unofficial repairs.",
            "data_wiping": "Back up important files and factory reset the phone.",
            "environmental_impact": "Recycling helps recover materials and reduce electronic waste.",
            "resale": "Resale value depends on condition, storage, and market demand.",
        },
        "m": {
            "common_issues": "Battery aging, charging issues, and software slowdown.",
            "repair_advice": "Get the battery or charging port inspected by a professional.",
            "reuse_donation": "Reuse the device for basic tasks or donate it if functional.",
            "recycling": "Send the device to a certified e-waste recycler.",
            "safety": "Do not use a swollen battery.",
            "data_wiping": "Back up data and perform a factory reset.",
            "environmental_impact": "Responsible recycling reduces e-waste and resource loss.",
            "resale": "Estimated resale depends on age, condition, and demand.",
        },
    },
    "apple": {
        "iphone": {
            "common_issues": "Battery health reduction, screen damage, and charging issues.",
            "repair_advice": "Contact Apple or an authorized service provider.",
            "reuse_donation": "Reuse as a camera, music player, or donate if working.",
            "recycling": "Use an authorized Apple or e-waste recycling program.",
            "safety": "Avoid using a damaged or swollen battery.",
            "data_wiping": "Back up data, sign out of accounts, and erase all content.",
            "environmental_impact": "Recycling helps recover valuable materials and reduce electronic waste.",
            "resale": "Value depends on model, storage, battery health, and condition.",
        },
        "ipad": {
            "common_issues": "Battery aging, screen damage, charging problems, and software issues.",
            "repair_advice": "Contact Apple or an authorized service provider for repair.",
            "reuse_donation": "Reuse it for studying, reading, media, or donate it if working.",
            "recycling": "Send the iPad to an authorized Apple or e-waste recycling program.",
            "safety": "Do not use the device if the battery is swollen or physically damaged.",
            "data_wiping": "Back up important data, sign out of Apple ID, and erase all content.",
            "environmental_impact": "Responsible recycling helps recover materials and reduces electronic waste.",
            "resale": "Value depends on model, storage, age, condition, and battery health.",
        },
        "macbook": {
            "common_issues": "Battery aging, keyboard or trackpad problems, screen damage, and software issues.",
            "repair_advice": "Contact Apple or an authorized service provider for inspection and repair.",
            "reuse_donation": "Continue using it for learning or office work, or donate it if functional.",
            "recycling": "Recycle through an authorized Apple or e-waste recycling program.",
            "safety": "Avoid using a damaged battery or damaged charging equipment.",
            "data_wiping": "Back up files, sign out of accounts, and erase the Mac before disposal.",
            "environmental_impact": "Proper recycling helps recover useful materials and reduces electronic waste.",
            "resale": "Value depends on model, year, storage, condition, and battery health.",
        },
        "watch": {
            "common_issues": "Battery aging, screen damage, charging problems, and software issues.",
            "repair_advice": "Contact Apple or an authorized service provider for assistance.",
            "reuse_donation": "Continue using it for fitness or notifications, or donate it if working.",
            "recycling": "Use an authorized Apple or e-waste recycling program.",
            "safety": "Do not use the device if the battery is swollen or physically damaged.",
            "data_wiping": "Back up required data, unpair the watch, and erase its content.",
            "environmental_impact": "Responsible recycling helps recover materials and reduce electronic waste.",
            "resale": "Value depends on model, age, condition, battery health, and demand.",
        },
    },
    "oppo": {
        "reno": {
            "common_issues": "Battery wear, screen damage, and charging problems.",
            "repair_advice": "Visit an authorized OPPO service center.",
            "reuse_donation": "Use the phone for learning or donate it if functional.",
            "recycling": "Recycle through an authorized e-waste collection center.",
            "safety": "Do not use damaged batteries or chargers.",
            "data_wiping": "Back up data and perform a factory reset.",
            "environmental_impact": "Proper recycling helps reduce environmental pollution.",
            "resale": "Resale depends on model, age, condition, and demand.",
        }
    },
    "oneplus": {
        "oneplus": {
            "common_issues": "Battery degradation, screen damage, and software problems.",
            "repair_advice": "Contact an authorized OnePlus service center.",
            "reuse_donation": "Reuse for entertainment or donate if working.",
            "recycling": "Send the device to an authorized recycler.",
            "safety": "Avoid using damaged batteries and chargers.",
            "data_wiping": "Back up files and perform a factory reset.",
            "environmental_impact": "Responsible recycling reduces electronic waste and resource loss.",
            "resale": "Estimated resale depends on condition, storage, and market demand.",
        }
    },
    "xiaomi": {
        "redmi": {
            "common_issues": "Battery aging, charging problems, and screen damage.",
            "repair_advice": "Visit an authorized Xiaomi service center.",
            "reuse_donation": "Reuse for basic tasks or donate the device.",
            "recycling": "Recycle through an authorized e-waste recycler.",
            "safety": "Do not use a swollen battery or damaged charger.",
            "data_wiping": "Back up data and perform a factory reset.",
            "environmental_impact": "Recycling helps conserve resources and reduce e-waste.",
            "resale": "Resale depends on model, age, condition, and market demand.",
        }
    },
}

CLEANUP_TIPS = [
    "Delete unnecessary downloads.",
    "Remove duplicate files.",
    "Organise files into folders.",
    "Delete unwanted emails.",
]

GREEN_TIPS = [
    "Repair devices before replacing them.",
    "Donate working electronics.",
    "Switch off devices when not needed.",
    "Use energy-saving settings.",
    "Recycle e-waste responsibly.",
]

FIELD_LABELS = [
    ("common_issues", "Common Issues"),
    ("repair_advice", "Repair Advice"),
    ("reuse_donation", "Reuse / Donation"),
    ("recycling", "Recycling Advice"),
    ("safety", "Safety Precautions"),
    ("data_wiping", "Data Wiping"),
    ("environmental_impact", "Environmental Impact"),
    ("resale", "Estimated Resale"),
]

# ----------------------------------------------------------------------
# Colors / fonts
# ----------------------------------------------------------------------
MOSS = "#2F4A3C"
MOSS_DARK = "#1C2E24"
PAPER = "#F1EDE2"
PAPER_DIM = "#E6E0D0"
CLAY = "#B5652E"
INK = "#20241F"

HEAD_FONT = ("Georgia", 18, "bold")
LABEL_FONT = ("Segoe UI", 10, "bold")
BODY_FONT = ("Segoe UI", 10)
RESULT_TITLE_FONT = ("Georgia", 14, "bold")
REC_FONT = ("Georgia", 16, "bold")


class GreenTechApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GreenTech")
        self.geometry("560x620")
        self.configure(bg=PAPER)
        self.minsize(480, 520)

        header = tk.Frame(self, bg=PAPER)
        header.pack(fill="x", padx=20, pady=(18, 10))
        tk.Label(header, text="GreenTech", font=HEAD_FONT, bg=PAPER, fg=INK).pack(anchor="w")
        tk.Label(
            header,
            text="Practical guidance for what to do with the devices you're done with.",
            font=BODY_FONT, bg=PAPER, fg="#5b5c53",
        ).pack(anchor="w")

        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("TNotebook", background=PAPER, borderwidth=0)
        style.configure("TNotebook.Tab", font=("Segoe UI", 9, "bold"), padding=(12, 8))
        style.map("TNotebook.Tab", background=[("selected", MOSS)], foreground=[("selected", PAPER)])

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        self.advisor_tab = tk.Frame(notebook, bg="white")
        self.info_tab = tk.Frame(notebook, bg="white")
        self.cleanup_tab = tk.Frame(notebook, bg="white")
        self.green_tab = tk.Frame(notebook, bg="white")

        notebook.add(self.advisor_tab, text="Device Advisor")
        notebook.add(self.info_tab, text="E-Waste Info")
        notebook.add(self.cleanup_tab, text="Digital Cleanup")
        notebook.add(self.green_tab, text="Green Computing")

        self._build_advisor_tab()
        self._build_info_tab()
        self._build_tips_tab(self.cleanup_tab, "Digital Cleanup Tips", CLEANUP_TIPS)
        self._build_tips_tab(self.green_tab, "Green Computing Tips", GREEN_TIPS)

    # ------------------------------------------------------------------
    # Tab 1: Device Advisor
    # ------------------------------------------------------------------
    def _build_advisor_tab(self):
        f = self.advisor_tab
        pad = {"padx": 20}

        tk.Label(f, text="Device Advisor", font=RESULT_TITLE_FONT, bg="white", fg=INK).pack(
            anchor="w", pady=(18, 14), **pad
        )

        tk.Label(f, text="Device name", font=LABEL_FONT, bg="white", fg=INK).pack(anchor="w", **pad)
        self.dv_name = tk.Entry(f, font=BODY_FONT)
        self.dv_name.pack(fill="x", pady=(2, 10), **pad)

        tk.Label(f, text="Years used", font=LABEL_FONT, bg="white", fg=INK).pack(anchor="w", **pad)
        self.dv_age = tk.Entry(f, font=BODY_FONT)
        self.dv_age.pack(fill="x", pady=(2, 10), **pad)

        tk.Label(f, text="Is the device working properly?", font=LABEL_FONT, bg="white", fg=INK).pack(
            anchor="w", **pad
        )
        self.dv_working = tk.StringVar(value="yes")
        row1 = tk.Frame(f, bg="white")
        row1.pack(anchor="w", pady=(2, 10), **pad)
        tk.Radiobutton(row1, text="Yes", variable=self.dv_working, value="yes", bg="white").pack(side="left")
        tk.Radiobutton(row1, text="No", variable=self.dv_working, value="no", bg="white").pack(side="left", padx=(12, 0))

        tk.Label(f, text="Does it have a major problem?", font=LABEL_FONT, bg="white", fg=INK).pack(
            anchor="w", **pad
        )
        self.dv_major = tk.StringVar(value="no")
        row2 = tk.Frame(f, bg="white")
        row2.pack(anchor="w", pady=(2, 10), **pad)
        tk.Radiobutton(row2, text="No", variable=self.dv_major, value="no", bg="white").pack(side="left")
        tk.Radiobutton(row2, text="Yes", variable=self.dv_major, value="yes", bg="white").pack(side="left", padx=(12, 0))

        tk.Button(
            f, text="Get recommendation", font=LABEL_FONT, bg=MOSS, fg="white",
            activebackground=MOSS_DARK, activeforeground="white", relief="flat",
            command=self._run_advisor,
        ).pack(anchor="w", pady=(6, 4), **pad)

        self.advisor_result = tk.Label(
            f, text="", font=BODY_FONT, bg=PAPER_DIM, fg=INK, justify="left",
            anchor="w", wraplength=480, padx=14, pady=12,
        )
        self.advisor_result.pack(fill="x", pady=(10, 10), **pad)

    def _run_advisor(self):
        name = self.dv_name.get().strip() or "Device"
        age_raw = self.dv_age.get().strip()
        try:
            age = int(age_raw)
            if age < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid input", "Enter a valid whole number of years used.")
            return

        working = self.dv_working.get()
        major_problem = self.dv_major.get()

        if working == "yes" and major_problem == "no":
            recommendation = "Continue using" if age <= 5 else "Reuse (consider donating or repurposing)"
        elif working == "no" and major_problem == "no":
            recommendation = "Repair"
        elif major_problem == "yes":
            recommendation = "Repair" if age <= 3 else "Recycle"
        else:
            recommendation = "Recycle"

        self.advisor_result.config(
            text=(
                f"Device: {name}\n"
                f"Age: {age} year(s)\n\n"
                f"Recommendation: {recommendation}\n\n"
                "Note: This is general guidance based on fixed rules only. "
                "It cannot identify the exact technical fault without professional inspection."
            )
        )

    # ------------------------------------------------------------------
    # Tab 2: E-Waste Information
    # ------------------------------------------------------------------
    def _build_info_tab(self):
        f = self.info_tab
        pad = {"padx": 20}

        tk.Label(f, text="E-Waste Information", font=RESULT_TITLE_FONT, bg="white", fg=INK).pack(
            anchor="w", pady=(18, 14), **pad
        )

        tk.Label(f, text="Brand", font=LABEL_FONT, bg="white", fg=INK).pack(anchor="w", **pad)
        self.ew_brand = ttk.Combobox(f, values=[b.title() for b in E_WASTE_DATA], state="readonly")
        self.ew_brand.pack(fill="x", pady=(2, 10), **pad)
        self.ew_brand.bind("<<ComboboxSelected>>", self._populate_series)

        tk.Label(f, text="Series", font=LABEL_FONT, bg="white", fg=INK).pack(anchor="w", **pad)
        self.ew_series = ttk.Combobox(f, values=[], state="readonly")
        self.ew_series.pack(fill="x", pady=(2, 10), **pad)

        tk.Button(
            f, text="Show information", font=LABEL_FONT, bg=MOSS, fg="white",
            activebackground=MOSS_DARK, activeforeground="white", relief="flat",
            command=self._run_info,
        ).pack(anchor="w", pady=(6, 4), **pad)

        self.info_result = tk.Label(
            f, text="", font=BODY_FONT, bg=PAPER_DIM, fg=INK, justify="left",
            anchor="w", wraplength=480, padx=14, pady=12,
        )
        self.info_result.pack(fill="both", expand=True, pady=(10, 10), **pad)

    def _populate_series(self, event=None):
        brand = self.ew_brand.get().lower()
        series_list = [s.title() for s in E_WASTE_DATA.get(brand, {})]
        self.ew_series.config(values=series_list)
        self.ew_series.set("")
        self.info_result.config(text="")

    def _run_info(self):
        brand = self.ew_brand.get().lower()
        series = self.ew_series.get().lower()
        if not brand or not series:
            messagebox.showerror("Missing selection", "Choose both a brand and a series.")
            return
        d = E_WASTE_DATA[brand][series]
        lines = [f"{brand.title()} — {series.title()}\n"]
        for key, label in FIELD_LABELS:
            lines.append(f"{label}: {d[key]}")
        self.info_result.config(text="\n\n".join(lines))

    # ------------------------------------------------------------------
    # Tabs 3 & 4: Tip lists
    # ------------------------------------------------------------------
    def _build_tips_tab(self, frame, title, tips):
        tk.Label(frame, text=title, font=RESULT_TITLE_FONT, bg="white", fg=INK).pack(
            anchor="w", padx=20, pady=(18, 14)
        )
        for tip in tips:
            row = tk.Frame(frame, bg="white")
            row.pack(anchor="w", fill="x", padx=20, pady=4)
            tk.Label(row, text="•", font=("Segoe UI", 12, "bold"), bg="white", fg=CLAY).pack(side="left")
            tk.Label(
                row, text=tip, font=BODY_FONT, bg="white", fg=INK,
                justify="left", wraplength=460,
            ).pack(side="left", padx=(8, 0))


if __name__ == "__main__":
    app = GreenTechApp()
    app.mainloop()
