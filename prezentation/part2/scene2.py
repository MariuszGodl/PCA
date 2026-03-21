from manim import *
from manim_slides import Slide

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

my_template = TexTemplate()
my_template.add_to_preamble(r"\usepackage{polski}")
my_template.add_to_preamble(r"\usepackage{amsmath}")
my_template.add_to_preamble(r"\usepackage{amsthm}")
my_template.add_to_preamble(r"\usepackage{physics}")
class Final2_2(Slide):
    def construct(self):
        # ---------------------------------------------------
        # PART 1: Perplexity
        # ---------------------------------------------------

        title = Text("Perplexity", font_size=40, color=BLUE).to_edge(UP)

        eq1 = MathTex(r"Perp(P_i) = 2^{H(P_i)}", tex_template=my_template)
        eq2 = MathTex(r"H(P_i) = -\sum_j p_{j|i}\log_2(p_{j|i})", tex_template=my_template)

        text = Tex(
            r"Interpretacja: liczba istotnych sąsiadów",
            tex_template=my_template
        )

        content = VGroup(eq1, eq2, text).arrange(DOWN, buff=0.6).next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(eq1))
        self.next_slide()
        self.play(Write(eq2))
        self.play(FadeIn(text))

        self.next_slide()
        self.clear()

        # ---------------------------------------------------
        # PART 2: Perplexity Evolution Animation
        # ---------------------------------------------------
        axes = Axes(
            x_range=[0, 1, 1],
            y_range=[0, 1, 1],
            x_length=6,
            y_length=6,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "include_tip": False,
                "font_size": 24,
            },
        ).shift(DOWN * 0.5)

        colors = [
            RED, GREEN, BLUE, YELLOW, PURPLE, 
            ORANGE, PINK, TEAL, DARK_BROWN, GREY,
        ]

        colorbar = VGroup()
        clabels = VGroup()
        for i, color in enumerate(colors):
            rect = Rectangle(
                width=0.6, height=0.3, color=color,
                fill_opacity=1, stroke_width=0,
            )
            label = Tex(f"{i}", color=WHITE).scale(0.4)
            colorbar.add(rect)
            clabels.add(label)

        colorbar.next_to(axes, direction=RIGHT, buff=0.5)
        colorbar.arrange(DOWN, buff=0.2).to_edge(RIGHT, buff=1.5)

        for idx, clabel in enumerate(clabels):
            clabel.next_to(colorbar[idx], direction=RIGHT, buff=0.3)

        data = np.load("data/30.npy")
        coordinates = data[:, :2]
        labels = data[:, 2]

        normalized_coordinates = (coordinates - coordinates.min(axis=0)) / (
            coordinates.max(axis=0) - coordinates.min(axis=0)
        )

        dots = VGroup()
        for i, (x, y) in enumerate(normalized_coordinates):
            dot = Dot(
                axes.c2p(x, y),
                color=colors[int(labels[i])],
                radius=0.025,
                fill_opacity=0.6,
            )
            dots.add(dot)

        perp_counter = MathTex("Perplexity = 30").scale(0.7).next_to(axes, UP)

        self.play(FadeIn(axes, colorbar, clabels, dots, perp_counter), run_time=2)
        self.wait(0.5)

        self.next_slide()

        for perp in range(40, 71, 10):
            data = np.load(f"data/{perp}.npy")
            coordinates = data[:, :2]
            labels = data[:, 2]

            normalized_coordinates = (coordinates - coordinates.min(axis=0)) / (
                coordinates.max(axis=0) - coordinates.min(axis=0)
            )

            new_dots = VGroup()
            for i, (x, y) in enumerate(normalized_coordinates):
                dot = Dot(
                    axes.c2p(x, y),
                    color=colors[int(labels[i])],
                    radius=0.025,
                    fill_opacity=0.6,
                )
                new_dots.add(dot)
            new_perp_counter = (
                MathTex(f"Perplexity = {perp}").scale(0.7).next_to(axes, UP)
            )

            self.play(
                Transform(dots, new_dots),
                Transform(perp_counter, new_perp_counter),
                run_time=1.8,
            )
            self.wait(0.4)

        self.next_slide()

        for perp in range(70, 101, 10):
            data = np.load(f"data/{perp}.npy")
            coordinates = data[:, :2]
            labels = data[:, 2]

            normalized_coordinates = (coordinates - coordinates.min(axis=0)) / (
                coordinates.max(axis=0) - coordinates.min(axis=0)
            )

            new_dots = VGroup()
            for i, (x, y) in enumerate(normalized_coordinates):
                dot = Dot(
                    axes.c2p(x, y),
                    color=colors[int(labels[i])],
                    radius=0.025,
                    fill_opacity=0.6,
                )
                new_dots.add(dot)
            new_perp_counter = (
                MathTex(f"Perplexity = {perp}").scale(0.7).next_to(axes, UP)
            )

            self.play(
                Transform(dots, new_dots),
                Transform(perp_counter, new_perp_counter),
                run_time=1.8,
            )
            self.wait(0.4)

        self.wait(0.6)
        
        self.next_slide()
        self.play(FadeOut(axes, dots, perp_counter, colorbar, clabels), run_time=1)
        self.clear() 


if __name__ == "__main__":
    scene = Final2_2()
    scene.render()