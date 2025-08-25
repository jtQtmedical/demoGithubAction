<?php
declare(strict_types=1);
use PHPUnit\Framework\TestCase; use App\Adder;
final class SampleTest extends TestCase { public function testSum(): void { $a=new Adder(); $this->assertSame(5,$a->sum(2,3)); } }
