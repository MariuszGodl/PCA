from manim import *
from manim_slides import Slide
import numpy as np


my_template = TexTemplate()
my_template.add_to_preamble(r"\usepackage{polski}")
my_template.add_to_preamble(r"\usepackage{amsmath}")
my_template.add_to_preamble(r"\usepackage{amsthm}")
my_template.add_to_preamble(r"\usepackage{physics}")

class Final2_1(Slide):
    def construct(self):
        
        # ==========================================================
        # Slide 1: Cel
        # ==========================================================
        title = Text("Cel", font_size=48, color=BLUE).to_edge(UP)

        text = Tex(
            r"Redukcja zbioru $\mathcal{X} = \{x_1,\ldots,x_n\}$\\",
            r"do $\mathcal{Y} = \{y_1,\ldots,y_n\}$",
            tex_template=my_template,
            font_size=36
        ).next_to(title, DOWN, buff=0.5)

        img1 = ImageMobject("./img/MNIST").scale_to_fit_height(2.5)
        img2 = ImageMobject("./img/TSNEembedding").scale_to_fit_height(2.5)

        images = Group(img1, img2)
        images.arrange(RIGHT, buff=0.8)
        images.next_to(text, DOWN, buff=0.5)

        caption = Tex(
            r"Projekcja zbioru MNIST na dwa wymiary",
            tex_template=my_template,
            font_size=30
        ).next_to(images, DOWN, buff=0.5)

        self.play(Write(title), Write(text))
        self.play(FadeIn(images))
        self.play(Write(caption))

        self.next_slide()
        self.clear()

        # ==========================================================
        # Slide 2: Prawdopodobieństwa Warunkowe
        # ==========================================================
        title_prob = Text("Prawdopodobieństwa Warunkowe", font_size=40, color=BLUE).to_edge(UP)

        desc = Tex(
            r"t-SNE zamienia odległości na prawdopodobieństwa\\",
            r"warunkowe określające podobieństwo punktów.",
            tex_template=my_template,
            font_size=32
        ).next_to(title_prob, DOWN)

        eq = MathTex(
            r"p_{j|i} = \frac{e^{-\|x_i - x_j\|^2 / 2\sigma_i^2}}{\sum_{k\neq i} e^{-\|x_i - x_k\|^2 / 2\sigma_i^2}}",
            tex_template=my_template
        ).next_to(desc, DOWN)

        note = Tex(r"$p_{i|i}=0$", tex_template=my_template).next_to(eq, DOWN)

        self.play(Write(title_prob))
        self.play(FadeIn(desc))
        self.play(Write(eq))
        self.play(Write(note))

        self.next_slide()
        self.clear()
        
        # ==========================================================
        # Slide 3: Symetria
        # ==========================================================
        title = Text("Symetria", font_size=40, color=BLUE).to_edge(UP)

        text = Tex(
            r"$p_{j|i} \neq p_{i|j}$, więc definiujemy rozkład symetryczny:",
            tex_template=my_template
        ).next_to(title, DOWN)

        eq = MathTex(
            r"p_{ij} = p_{ji} = \frac{p_{i|j}+p_{j|i}}{2n}",
            tex_template=my_template
        ).next_to(text, DOWN)

        self.play(Write(title), FadeIn(text))
        self.play(Write(eq))

        self.next_slide()
        self.clear()

        # ==========================================================
        # Slide 4: Rozkład niskowymiarowy
        # ==========================================================
        title = Text("Rozkład w Niskowymiarowej Przestrzeni", font_size=38, color=BLUE).to_edge(UP)

        desc = Tex(
            r"Używamy rozkładu t-Studenta:",
            tex_template=my_template
        ).next_to(title, DOWN)

        eq = MathTex(
            r"q_{ij} = \frac{(1 + \|y_i - y_j\|^2)^{-1}}{\sum_{k\neq l} (1 + \|y_k - y_l\|^2)^{-1}}",
            tex_template=my_template
        ).next_to(desc, DOWN)

        note = Tex(r"$q_{ii}=0$", tex_template=my_template).next_to(eq, DOWN)

        self.play(Write(title))
        self.play(Write(desc))
        self.play(Write(eq))
        self.play(Write(note))

        self.next_slide()
        self.clear()
        
        # ==========================================================
        # Slide 5: Introduction of 2D points and distances
        # ==========================================================
        central_dot = Dot(np.array([0, 0, 0]), color=RED, radius=0.15)
        pt1 = np.array([1.0, 1.6, 0])
        pt2 = np.array([-1.15, 0.9, 0])
        pt3 = np.array([-1.8, -1.2, 0])
        pt4 = np.array([0.9, -1.1, 0])
        pt5 = np.array([0.7, 2.2, 0])

        dot1 = Dot(pt1, color=BLUE, radius=0.15)
        dot2 = Dot(pt2, color=BLUE, radius=0.15)
        dot3 = Dot(pt3, color=BLUE, radius=0.15)
        dot4 = Dot(pt4, color=BLUE, radius=0.15)
        dot5 = Dot(pt5, color=BLUE, radius=0.15)

        labels = VGroup(
            MathTex("x_i").next_to(central_dot, RIGHT), 
            MathTex("x_1").next_to(dot1, UP),
            MathTex("x_2").next_to(dot2, UP),
            MathTex("x_3").next_to(dot3, UP),
            MathTex("x_4").next_to(dot4, UP),
            MathTex("x_5").next_to(dot5, UP),
        )

        dots = VGroup(dot1, dot2, dot3, dot4, dot5)

        self.play(Create(central_dot))
        self.play(LaggedStartMap(Create, dots, lag_ratio=0.5), run_time=2)
        self.play(FadeIn(labels))

        arrows = VGroup(*[
            DoubleArrow(
                central_dot.get_center(), dot.get_center(),
                color=WHITE, buff=0.15, max_tip_length_to_length_ratio=0.15, stroke_width=2
            ) for dot in dots
        ])

        scatter_plot = VGroup(central_dot, dots, arrows, labels)

        self.play(LaggedStart(*[Create(arrow) for arrow in arrows], lag_ratio=0.5), run_time=2)
        self.wait(0.8)

        # ==========================================================
        # Slide 6: Map distances to a Gaussian (Single Equation)
        # ==========================================================
        self.next_slide()

        self.play(scatter_plot.animate.scale(0.6).to_edge(LEFT, buff=1.0))

        axes = (
            Axes(
                x_range=[0, 3, 1],
                y_range=[0, 1.2, 0.2],
                axis_config={
                    "color": WHITE,
                    "include_numbers": True,
                    "include_tip": False,
                    "font_size": 24,
                },
            )
            .scale(0.7)
            .to_edge(RIGHT, buff=1.0)
        )

        def gaussian(x):
            return np.exp(-(x**2) / 2)

        gaussian_curve = axes.plot(lambda x: gaussian(x), color=WHITE)

        points = [pt1, pt2, pt3, pt4, pt5]
        distances = [np.linalg.norm(pt) for pt in points]
        
        point_dots = [
            Dot(axes.c2p(x, 0), color=BLUE, radius=0.1, fill_opacity=0.8)
            for x in distances
        ]

        dashed_lines = []
        intersection_points = []
        for x in distances:
            y = gaussian(x)
            intersection = axes.c2p(x, y)
            intersection_points.append(intersection)
            dashed_line = DashedLine(axes.c2p(x, 0), intersection, color=WHITE)
            dashed_lines.append(dashed_line)

        intersection_dots = [
            Dot(point, color=BLUE, radius=0.1, fill_opacity=0.8)
            for point in intersection_points
        ]
        central_point = Dot(axes.c2p(0, 0), color=RED, radius=0.2, fill_opacity=0.8)

        self.play(FadeIn(axes, central_point))

        self.play(Create(gaussian_curve))
        self.play(*[Create(dot) for dot in point_dots])

        self.wait(0.4)

        self.play(Indicate(point_dots[0], scale_factor=2.2, color=BLUE), run_time=1.8)
        self.play(Indicate(central_point, scale_factor=1.4, color=RED), run_time=1.8)

        self.wait(0.5)

        self.play(*[Create(line) for line in dashed_lines])
        self.play(*[Create(dot) for dot in intersection_dots])

        gaussian_formula2d = MathTex(
            r"p_{j|i} = \frac{e^{-\|x_i - x_j\|^2 / 2", 
            r"\sigma_i", 
            r"^2}}{\sum_{k\neq i} e^{-\|x_i - x_k\|^2 / 2\sigma_i^2}}",
            tex_template=my_template
        ).to_corner(UR, buff=1.0)

        self.play(Write(gaussian_formula2d), run_time=2)
        self.wait(0.6)

        # ==========================================================
        # Slide 7: Standard deviation influences the spread
        # ==========================================================
        self.next_slide()
        self.wait()
        
        rect = SurroundingRectangle(gaussian_formula2d[1], buff=0.1, color=YELLOW)
        self.play(Create(rect))

        self.play(FadeOut(*intersection_dots, *dashed_lines))
        self.wait(0.6)

        def gaussian_wide(x):
            return np.exp(-(x**2) / 8)

        def gaussian_narrow(x):
            return np.exp(-(x**2) / 0.5)

        gaussian_curve_wide = axes.plot(lambda x: gaussian_wide(x), color=WHITE)
        gaussian_curve_narrow = axes.plot(lambda x: gaussian_narrow(x), color=WHITE)

        label_increase = MathTex(r"\text{Increase } \sigma_i", color=YELLOW).next_to(axes, UP, buff=-1.5)
        label_decrease = MathTex(r"\text{Decrease } \sigma_i", color=YELLOW).move_to(label_increase)

        self.wait(1)

        self.play(Write(label_increase))
        self.play(Transform(gaussian_curve, gaussian_curve_wide), run_time=2)
        self.wait(0.3)

        self.play(Transform(label_increase, label_decrease))
        self.play(Transform(gaussian_curve, gaussian_curve_narrow), run_time=2)

        self.play(FadeOut(rect, label_increase), run_time=0.6)
        self.wait(0.7)
        # ==========================================================
        # Slide 8: Low dimension space with random points
        # ==========================================================
        self.next_slide()
        self.clear()

        nb_line = NumberLine(
            x_range=[-2, 2, 1],
            length=8,
            include_numbers=True,
            include_tip=False,
            color=WHITE,
            font_size=24,
        )

        central_point = Dot(nb_line.n2p(0), color=RED, radius=0.2, fill_opacity=0.8)
        pt1_1d = np.array([0.3])
        pt2_1d = np.array([-0.5])
        pt3_1d = np.array([1.2])
        pt4_1d = np.array([-0.9])
        pt5_1d = np.array([1.6])

        dot1_1d = Dot(nb_line.n2p(pt1_1d[0]), color=BLUE, radius=0.1, fill_opacity=0.8)
        dot2_1d = Dot(nb_line.n2p(pt2_1d[0]), color=BLUE, radius=0.1, fill_opacity=0.8)
        dot3_1d = Dot(nb_line.n2p(pt3_1d[0]), color=BLUE, radius=0.1, fill_opacity=0.8)
        dot4_1d = Dot(nb_line.n2p(pt4_1d[0]), color=BLUE, radius=0.1, fill_opacity=0.8)
        dot5_1d = Dot(nb_line.n2p(pt5_1d[0]), color=BLUE, radius=0.1, fill_opacity=0.8)

        dots_1d = VGroup(dot1_1d, dot2_1d, dot3_1d, dot4_1d, dot5_1d)

        labels_1d = VGroup(
            MathTex("y_i").next_to(central_point, UP),
            MathTex("y_1").next_to(dot1_1d, UP),
            MathTex("y_2").next_to(dot2_1d, UP),
            MathTex("y_3").next_to(dot3_1d, UP),
            MathTex("y_4").next_to(dot4_1d, UP),
            MathTex("y_5").next_to(dot5_1d, UP),
        )

        self.play(FadeIn(nb_line, central_point))
        self.play(LaggedStartMap(Create, dots_1d, lag_ratio=0.5), run_time=2)
        self.play(FadeIn(labels_1d))
        self.wait(0.3)

        scatter_plot1d = VGroup(nb_line, central_point, dots_1d, labels_1d)
        self.play(scatter_plot1d.animate.scale(0.4).to_edge(LEFT, buff=0.6))

        axes_1d = (
            Axes(
                x_range=[0, 3, 1],
                y_range=[0, 1.2, 0.2],
                axis_config={
                    "color": WHITE,
                    "include_numbers": True,
                    "include_tip": False,
                    "font_size": 24,
                },
            )
            .scale(0.7)
            .to_edge(RIGHT, buff=1.0)
        )

        gaussian_curve_1d = axes_1d.plot(lambda x: gaussian(x), color=WHITE)

        points_1d = [pt1_1d, pt2_1d, pt3_1d, pt4_1d, pt5_1d]
        distances_1d = [np.linalg.norm(pt) for pt in points_1d]

        point_dots_1d = [
            Dot(axes_1d.c2p(x, 0), color=BLUE, radius=0.1, fill_opacity=0.8)
            for x in distances_1d
        ]

        dashed_lines_1d = []
        intersection_points_1d = []
        for x in distances_1d:
            y = gaussian(x)
            intersection = axes_1d.c2p(x, y)
            intersection_points_1d.append(intersection)
            dashed_line = DashedLine(axes_1d.c2p(x, 0), intersection, color=WHITE)
            dashed_lines_1d.append(dashed_line)

        intersection_dots_1d = [
            Dot(point, color=BLUE, radius=0.1, fill_opacity=0.8)
            for point in intersection_points_1d
        ]
        central_point_1d = Dot(axes_1d.c2p(0, 0), color=RED, radius=0.2, fill_opacity=0.8)

        self.play(FadeIn(axes_1d, central_point_1d))

        self.play(Create(gaussian_curve_1d), run_time=2)
        self.play(*[Create(dot) for dot in point_dots_1d])
        self.wait(0.5)
        self.play(*[Create(line) for line in dashed_lines_1d])
        self.play(*[Create(dot) for dot in intersection_dots_1d])
        self.wait(1)

        gaussian_formula1d = MathTex(
            r"q_{ij} = \frac{(1 + \|y_i - y_j\|^2)^{-1}}{\sum_{k\neq l} (1 + \|y_k - y_l\|^2)^{-1}}",
            tex_template=my_template
        ).to_corner(UR, buff=1.0)

        self.play(FadeIn(gaussian_formula1d))
        self.wait()

        # ==========================================================
        # Slide 9: Gaussian vs t-Student
        # ==========================================================
        self.next_slide()
        self.clear()

        title_dist = Text("Rozkład Gaussa vs t-Studenta", font_size=42, color=BLUE).to_edge(UP)

        ax_dist = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1.2, 0.2],
            axis_config={"color": WHITE, "include_numbers": True},
        ).scale(0.8).next_to(title_dist, DOWN, buff=0.5)

        gauss_dist_curve = ax_dist.plot(lambda x: np.exp(-x**2), color=YELLOW)
        t_dist_curve = ax_dist.plot(lambda x: 1 / (1 + x**2), color=RED)

        gauss_dist_label = Text("Gaussian", color=YELLOW, font_size=24).next_to(gauss_dist_curve, UP, buff=0.1).shift(RIGHT*1.5)
        t_dist_label = Text("t-Student", color=RED, font_size=24).next_to(t_dist_curve, UP, buff=0.1).shift(RIGHT*3.5 + UP*0.5)

        self.play(Write(title_dist))
        self.play(FadeIn(ax_dist))
        
        self.play(Create(gauss_dist_curve), Write(gauss_dist_label), run_time=1.5)
        self.play(Create(t_dist_curve), Write(t_dist_label), run_time=1.5)

        tail_anchor1 = Dot(ax_dist.c2p(-3.5, 0.1)).set_opacity(0)
        tail_anchor2 = Dot(ax_dist.c2p(3.5, 0.1)).set_opacity(0)

        tail_rect1 = SurroundingRectangle(tail_anchor1, buff=0.6, color=WHITE)
        tail_rect2 = SurroundingRectangle(tail_anchor2, buff=0.6, color=WHITE)
        
        self.play(Create(tail_rect1), Create(tail_rect2))
        self.wait(2)
        # ==========================================================
        # Slide 10: Display the two probability distributions
        # ==========================================================
        self.next_slide()
        self.clear()

        scatter_plot1d.scale(1.3).move_to(2 * DOWN + 3.5 * LEFT)
        gaussian_formula1d.move_to(2 * UP + 3.5 * LEFT)

        scatter_plot.remove(arrows)
        scatter_plot.move_to(DOWN + 3.5 * RIGHT)

        gaussian_formula2d_final = MathTex(
            r"p_{j|i} = \frac{e^{-\|x_i - x_j\|^2 / 2\sigma_i^2}}{\sum_{k\neq i} e^{-\|x_i - x_k\|^2 / 2\sigma_i^2}}",
            tex_template=my_template
        ).move_to(2 * UP + 3.5 * RIGHT)

        self.play(
            FadeIn(scatter_plot1d, gaussian_formula1d, scatter_plot, gaussian_formula2d_final)
        )

        self.next_slide()
        self.clear()

if __name__ == "__main__":
    scene = Final2_1()
    scene.render()