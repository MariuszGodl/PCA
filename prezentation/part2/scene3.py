from manim import *
from manim_slides import Slide
import numpy as np

my_template = TexTemplate()
my_template.add_to_preamble(r"\usepackage{polski}")
my_template.add_to_preamble(r"\usepackage{amsmath}")
my_template.add_to_preamble(r"\usepackage{amsthm}")
my_template.add_to_preamble(r"\usepackage{physics}")
my_template.add_to_preamble(r"\DeclareMathOperator{\const}{const.}")


class Final2_3(Slide):
    def construct(self):

        # ==========================================
        # SLIDE 1: KL formula
        # ==========================================
        title = Text("Mierzenie Podobieństwa Rozkładów", font_size=40, color=BLUE).to_edge(UP)

        desc_kl1 = Tex("Jest to metoda mierzenia rozbieżności dwóch rozkładów prawdopodobieństwa:", tex_template=my_template, font_size=32)
        eq = MathTex(
            r"KL(P||Q) = \sum_{i}\sum_{j} p_{ij} \log\left(\frac{p_{ij}}{q_{ij}}\right).",
            tex_template=my_template
        )
        
        desc_kl2 = Tex("Będziemy ją traktować jak funkcję kosztu:", tex_template=my_template, font_size=32)
        cost = MathTex(
            r"C = KL(P||Q).",
            tex_template=my_template
        )
        
        content = VGroup(desc_kl1, eq, desc_kl2, cost).arrange(DOWN, buff=0.6).next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        self.play(Write(desc_kl1))
        self.play(Write(eq))
        self.next_slide()
        self.play(Write(desc_kl2))
        self.play(Write(cost))
        
        self.next_slide()
        self.clear()

        # ==========================================
        # SLIDE 2: Display the distributions along with the KL
        # ==========================================
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 1, 0.2],
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "include_tip": False,
                "font_size": 24,
            },
        ).scale(0.7)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        mean1, std1 = 0, 1
        mean2, std2 = 2, 1

        gaussian1 = lambda x: np.exp(-((x - mean1) ** 2) / (2 * std1**2)) / (
            std1 * np.sqrt(2 * np.pi)
        )
        gaussian2 = lambda x: np.exp(-((x - mean2) ** 2) / (2 * std2**2)) / (
            std2 * np.sqrt(2 * np.pi)
        )

        legend = VGroup(
            Line(start=ORIGIN, end=0.3 * RIGHT, color=GREEN).shift(LEFT + UP),
            Tex("P").next_to(
                Line(start=ORIGIN, end=0.3 * RIGHT, color=GREEN).shift(LEFT + UP), RIGHT
            ),
            Line(start=ORIGIN, end=0.3 * RIGHT, color=RED).shift(LEFT + 0.5 * UP),
            Tex("Q").next_to(
                Line(start=ORIGIN, end=0.3 * RIGHT, color=RED).shift(LEFT + 0.5 * UP), RIGHT,
            ),
            Line(start=ORIGIN, end=0.3 * RIGHT, color=BLUE).shift(LEFT),
            Tex("KL divergence").next_to(
                Line(start=ORIGIN, end=0.3 * RIGHT, color=BLUE).shift(LEFT), RIGHT
            ),
        ).move_to(axes.get_corner(UL))

        self.play(FadeIn(axes, legend, axes_labels), run_time=1.5)

        graph1 = axes.plot(gaussian1, color=GREEN)
        graph2 = axes.plot(gaussian2, color=RED)
        
        self.play(Create(graph1), Create(graph2), run_time=2)

        kl_div = lambda x: gaussian1(x) * np.log(gaussian1(x) / gaussian2(x))
        graph3 = axes.plot(kl_div, color=BLUE)
        area = axes.get_area(graph3, x_range=[-5, 5], color=BLUE, opacity=0.3)
        
        self.play(Create(graph3), Create(area), run_time=2)
        self.play(FadeOut(area), run_time=0.6)

        mean2 = 3
        self.play(
            graph2.animate.become(axes.plot(gaussian2, color=RED)),
            graph3.animate.become(axes.plot(kl_div, color=BLUE)),
            run_time=2,
        )
        self.wait(2)
        
        mean2 = 1
        self.play(
            graph2.animate.become(axes.plot(gaussian2, color=RED)),
            graph3.animate.become(axes.plot(kl_div, color=BLUE)),
            run_time=2,
        )
        self.wait(0.6)
        
        mean1 = 0
        mean2 = 0
        self.play(
            graph1.animate.become(axes.plot(gaussian1, color=GREEN)),
            graph2.animate.become(axes.plot(gaussian2, color=RED)),
            graph3.animate.become(axes.plot(kl_div, color=BLUE)),
            run_time=3,
        )
        
        self.next_slide()
        self.play(
            FadeOut(axes, legend, graph1, graph2, graph3, axes_labels),
            run_time=1,
        )
        self.clear()

        # ==========================================================
        # Slide 3: Gradient Funkcji Kosztu (Extended matching LaTeX)
        # ==========================================================
        title = Text("Gradient Funkcji Kosztu", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))

        desc_c1 = Tex(r"Spróbujemy zobaczyć jak zmienia się błąd, przy przesunięciu\\jednego punktu w niskowymiarowej mapie -- $\pdv{C}{y_i}$.", tex_template=my_template, font_size=32)

        eq_c1 = MathTex(
            r"C = \sum_{i}\sum_{j\neq i} p_{ij} \log\left(\frac{p_{ij}}{q_{ij}}\right)",
            r" = \underbrace{\sum_{i}\sum_{j\neq i} p_{ij} \log(p_{ij})}_{\const}",
            r" - \sum_{i}\sum_{j\neq i} p_{ij}\log(q_{ij})",
            tex_template=my_template
        ).scale(0.7)
        
        VGroup(desc_c1, eq_c1).arrange(DOWN, buff=0.6).next_to(title, DOWN, buff=1.0)
        
        self.play(Write(desc_c1))
        self.next_slide()

        for part in eq_c1:
            self.play(Write(part))
            self.next_slide()

        self.play(FadeOut(desc_c1), eq_c1.animate.shift(UP * 2))
        
        desc_defs = Tex("Dodatkowo wprowadzimy oznaczenia:", tex_template=my_template, font_size=32)
        
        eq_defs = MathTex(
            r"w_{ij} = (1 + \|y_i - y_j \|^2)^{-1},",
            r"\qquad Z = \sum_{k}\sum_{l\neq k} w_{kl},",
            r"\qquad q_{ij} = \frac{w_{ij}}{Z}",
            tex_template=my_template
        ).scale(0.7)
        
        eq_c2 = MathTex(
            r"C = \const",
            r" - \sum_{k}\sum_{k\neq l} p_{kl} \log(w_{kl})",
            r" + \sum_{k}\sum_{k\neq l} p_{kl} \log(Z)",
            tex_template=my_template
        ).scale(0.7)
        
        VGroup(desc_defs, eq_defs, eq_c2).arrange(DOWN, buff=0.6).next_to(eq_c1, DOWN, buff=0.6)
        
        self.play(Write(desc_defs))
        self.next_slide()
        
        for part in eq_defs:
            self.play(Write(part))
            self.next_slide()
            
        for part in eq_c2:
            self.play(Write(part))
            self.next_slide()
            
        self.clear()

        self.add(title)
        
        desc_dw = Tex("Na początku obliczymy pochodne $w_{ij}$ i $Z$:", tex_template=my_template, font_size=32)
        eq_dw = MathTex(
            r"\pdv{w_{ij}}{y_i} = -(1+\|y_i - y_j\|^2)^{-2} \cdot \pdv{(\|y_i - y_j\|^2)}{y_i}",
            r" = -2 w_{ij}^2 (y_i - y_j)",
            tex_template=my_template
        ).scale(0.7)
        
        desc_dz = Tex(r"Ponieważ $Z$ jest sumą wszystkich par, $y_i$ pojawia się tylko wtedy, gdy\\$k=i$ lub $l=i$, a ponieważ $w_{ij} = w_{ji}$, mnożymy wynik przez 2:", tex_template=my_template, font_size=28)
        eq_dz = MathTex(
            r"\pdv{Z}{y_i} = 2 \sum_{j\neq i} \pdv{w_{ij}}{y_i}",
            r" = -4\sum_{j\neq i} w_{ij}^2 (y_i - y_j)",
            tex_template=my_template
        ).scale(0.7)
        
        VGroup(desc_dw, eq_dw, desc_dz, eq_dz).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(desc_dw))
        self.next_slide()
        for part in eq_dw:
            self.play(Write(part))
            self.next_slide()
            
        self.play(Write(desc_dz))
        self.next_slide()
        for part in eq_dz:
            self.play(Write(part))
            self.next_slide()
            
        self.clear()

        self.add(title)
        
        desc_base = Tex("Teraz możemy różniczkować całą funkcję $C$:", tex_template=my_template, font_size=32)
        eq_dc_base = MathTex(
            r"\pdv{C}{y_i} = -\sum_{k}\sum_{l\neq k} p_{kl}\pdv{\log(w_{kl})}{y_i}",
            r" + \sum_{k}\sum_{l\neq k} p_{kl}\pdv{\log(Z)}{y_i}",
            tex_template=my_template
        ).scale(0.7)
        
        eq_dc1 = MathTex(
            r"\pdv{C}{y_i} = -\underbrace{\sum_{k}\sum_{l\neq k} \frac{p_{kl}}{w_{kl}}\pdv{w_{kl}}{y_i}}_{I_1}",
            r" +\underbrace{ \sum_{k}\sum_{l\neq k} p_{kl} \frac{1}{Z} \cdot \pdv{Z}{y_i}}_{I_2}",
            tex_template=my_template
        ).scale(0.7)
        
        desc_I1 = Tex(r"Pochodna $\pdv{w_{kl}}{y_i}$ jest różna od zera tylko gdy $k=i$ lub $l=i$:", tex_template=my_template, font_size=28)
        eq_I1 = MathTex(
            r"I_1 = 2\sum_{j\neq i} \frac{p_{ij}}{w_{ij}} \pdv{w_{ij}}{y_i}",
            r" = -4\sum_{j\neq i}p_{ij} w_{ij}(y_i - y_j)",
            tex_template=my_template
        ).scale(0.7)
        
        VGroup(desc_base, eq_dc_base, eq_dc1, desc_I1, eq_I1).arrange(DOWN, buff=0.4).next_to(title, DOWN, buff=0.4)
        
        self.play(Write(desc_base))
        self.next_slide()
        for part in eq_dc_base:
            self.play(Write(part))
            self.next_slide()
            
        for part in eq_dc1:
            self.play(Write(part))
            self.next_slide()
            
        self.play(Write(desc_I1))
        self.next_slide()
        for part in eq_I1:
            self.play(Write(part))
            self.next_slide()
            
        self.clear()

        self.add(title)
        
        desc_I2 = Tex(r"Zauważmy, że $Z$ nie zależy od indeksów sumy oraz $\sum_{k, l} p_{kl} = 1$:", tex_template=my_template, font_size=28)
        eq_I2 = MathTex(
            r"I_2 = \sum_{k}\sum_{l\neq k} p_{kl} \frac{1}{Z} \pdv{Z}{y_i}",
            r" = \frac{1}{Z} \pdv{Z}{y_i}",
            r" = -4\sum_{j\neq i} q_{ij} w_{ij}(y_i - y_j)",
            tex_template=my_template
        ).scale(0.7)
        
        desc_dc2 = Tex("Dzięki temu otrzymujemy:", tex_template=my_template, font_size=32)
        eq_dc2 = MathTex(
            r"\pdv{C}{y_i} = -I_1 + I_2",
            r" = 4\sum_{j\neq i}(p_{ij} - q_{ij}) w_{ij} (y_i - y_j)",
            tex_template=my_template
        ).scale(0.7)
        
        eq_dc3 = MathTex(
            r"\pdv{C}{y_i}",
            r" = 4\sum_{j\neq i} (p_{ij}-q_{ij})(1+\|y_i - y_j\|^2)^{-1}(y_i - y_j)",
            tex_template=my_template
        ).scale(0.7)
        
        VGroup(desc_I2, eq_I2, desc_dc2, eq_dc2, eq_dc3).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(desc_I2))
        self.next_slide()
        for part in eq_I2:
            self.play(Write(part))
            self.next_slide()
            
        self.play(Write(desc_dc2))
        self.next_slide()
        for part in eq_dc2:
            self.play(Write(part))
            self.next_slide()
            
        for part in eq_dc3:
            self.play(Write(part))
            self.next_slide()
            
        self.clear()

        # ==========================================
        # SLIDE 4: Show the low-dimension representation evolving
        # ==========================================
        np.random.seed(0)

        points_2d_cluster1 = np.random.randn(10, 2) * 0.5 + np.array([-2, 2])
        points_2d_cluster2 = np.random.randn(10, 2) * 0.5 + np.array([2, 2])
        points_2d_cluster3 = np.random.randn(10, 2) * 0.5 + np.array([0, -2])
        points_2d_cluster4 = np.random.randn(10, 2) * 0.5 + np.array([2, -2])

        points_2d = np.vstack(
            [
                points_2d_cluster1,
                points_2d_cluster2,
                points_2d_cluster3,
                points_2d_cluster4,
            ]
        )

        points_1d = np.random.uniform(-3, 3, (40, 1))

        axes_2d = (
            Axes(
                x_range=[-5, 5, 1],
                y_range=[-5, 5, 1],
                axis_config={
                    "color": WHITE,
                    "include_numbers": True,
                    "include_tip": False,
                    "font_size": 24,
                },
            )
            .scale(0.5)
            .shift(3 * LEFT)
        )

        points_2d_plot = VGroup(
            *[
                Dot(
                    point=axes_2d.coords_to_point(x, y),
                    color=color,
                    radius=0.06,
                    fill_opacity=0.6,
                )
                for (x, y), color in zip(
                    points_2d,
                    [BLUE] * 10 + [GREEN] * 10 + [RED] * 10 + [YELLOW] * 10
                )
            ]
        )

        number_line = (
            NumberLine(x_range=[-5, 5, 1], include_numbers=True)
            .scale(0.5)
            .shift(3 * RIGHT)
        )

        points_1d_plot = VGroup(
            *[
                Dot(point=number_line.n2p(x), radius=0.06, fill_opacity=0.6)
                for x in points_1d
            ]
        )

        def compute_gradient(points_1d, points_2d):
            n_points = len(points_1d)
            gradients = np.zeros_like(points_1d)
            for i in range(n_points):
                for j in range(n_points):
                    if i != j:
                        y_i, y_j = points_2d[i], points_2d[j]
                        x_i, x_j = points_1d[i], points_1d[j]

                        p_ij = np.exp(-np.linalg.norm(x_i - x_j) ** 2)
                        q_ij = np.exp(-np.linalg.norm(y_i - y_j) ** 2)

                        p_ij /= np.sum(
                            [
                                np.exp(-np.linalg.norm(x_i - points_1d[k]) ** 2)
                                for k in range(n_points)
                            ]
                        )
                        q_ij /= np.sum(
                            [
                                np.exp(-np.linalg.norm(y_i - points_2d[k]) ** 2)
                                for k in range(n_points)
                            ]
                        )
                        gradient = 2 * (p_ij - q_ij) * (x_i - x_j)
                        gradients[i] += gradient
            return gradients

        num_iterations = 80

        self.play(FadeIn(axes_2d))
        self.play(Create(points_2d_plot))
        self.wait(1)
        
        self.play(FadeIn(number_line))
        self.play(Create(points_1d_plot))
        
        iteration_counter = Tex("Iteration: 0").next_to(number_line, UP, buff=2)

        for i in range(num_iterations):
            gradients = compute_gradient(points_1d, points_2d)
            points_1d += 0.1 * gradients

            points_1d_transformed_plot = VGroup(
                *[
                    Dot(point=number_line.n2p(x), radius=0.06, fill_opacity=0.6)
                    for x in points_1d
                ]
            )
            new_iteration_counter = Tex(f"Iteration: {i}").next_to(
                number_line, UP, buff=2
            )
            self.play(
                Transform(points_1d_plot, points_1d_transformed_plot),
                Transform(iteration_counter, new_iteration_counter),
                run_time=0.2,
            )

        self.next_slide()
        self.play(
            FadeOut(
                axes_2d,
                points_2d_plot,
                number_line,
                points_1d_plot,
                iteration_counter,
            ),
            run_time=1,
        )
        self.clear()

        # ==========================================
        # SLIDE 5: Algorytm (Smaller font & spacing)
        # ==========================================
        algo_title = Text("Cały Algorytm", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(algo_title))

        data_txt = Tex(
            r"\textbf{Dane:} wielowymiarowy zbiór $\mathcal{X} = \{x_1, x_2, \ldots, x_n\}$", 
            tex_template=my_template, 
            font_size=28
        ).to_edge(LEFT).shift(UP*2.5 + RIGHT*0.5)
        
        params_txt = Tex(
            r"\textbf{Parametry:} \textit{Perplexity}; ilość kroków $T$; \\ moment pędu $\alpha(t)$; szybkość uczenia $\eta$", 
            tex_template=my_template, 
            font_size=28
        ).next_to(data_txt, DOWN, aligned_edge=LEFT, buff=0.15)
        
        res_txt = Tex(
            r"\textbf{Rezultat:} niskowymiarowa mapa $\mathcal{Y}^{(t)} = \{y_1, y_2, \ldots, y_n\}$", 
            tex_template=my_template, 
            font_size=28
        ).next_to(params_txt, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(data_txt))
        self.play(Write(params_txt))
        self.play(Write(res_txt))

        algo_lines = VGroup(
            Tex(r"1. Oblicz prawdopodobieństwa $p_{j|i}$, z ustaloną wartością \emph{perplexity}", tex_template=my_template, font_size=28),
            Tex(r"2. Ustal $p_{ij} = \frac{p_{j|i} + p_{i|j}}{2n}$", tex_template=my_template, font_size=28),
            Tex(r"3. Wybierz stan początkowy $\mathcal{Y}^{(0)}$ z $\mathcal{N}(0, 10^{-4}I)$", tex_template=my_template, font_size=28),
            Tex(r"4. \textbf{for} $t=1$ \textbf{to} $T$ \textbf{do}", tex_template=my_template, font_size=28),
            Tex(r"Oblicz niskowymiarowe prawdopodobieństwa $q_{ij}$", tex_template=my_template, font_size=28),
            Tex(r"Oblicz Gradient $\frac{\partial C}{\partial \mathcal{Y}}$", tex_template=my_template, font_size=28),
            Tex(r"Ustal $\mathcal{Y}^{(t)} = \mathcal{Y}^{(t-1)} + \eta \frac{\partial C}{\partial \mathcal{Y}} + \alpha(t) \left( \mathcal{Y}^{(t-1)} - \mathcal{Y}^{(t-2)} \right)$", tex_template=my_template, font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(res_txt, DOWN, aligned_edge=LEFT, buff=0.3).shift(RIGHT*0.5)

        for i in range(4, 7):
            algo_lines[i].shift(RIGHT * 1.0)

        for line in algo_lines:
            self.play(Write(line))
            self.next_slide() 
        
        self.next_slide()
        self.clear()

if __name__ == "__main__":
    scene = Final2_3()
    scene.render()